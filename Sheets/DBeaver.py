import gspread #Biblioteca para manipularmos o Google Sheets
from google.oauth2.service_account import Credentials #Importando o uso das credenciais, sem elas não podemos manipular as planilhas
import psycopg2 #Biblioteca para termos acesso ao PsotgreSql
from psycopg2.extras import execute_values #Importando uma função da biblioteca para extrairmos os valores
from time import sleep #Importando o sleep, que atua de forma semelhante ao delay no C
import os #Sistema Operacional conexão com o Python
import datetime #Biblioteca para conseguirmos manipular dados com valores de tempo presentes no banco de dados

# Configuração do Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = './Apontar.json'  # Substitua pelo caminho do arquivo de credenciais
SPREADSHEET_ID = '13MaEB6QYdctMTgkh6GZTmMQfY78AsMNwWqPuAppUTPw'

# Configurar acesso ao Google Sheets
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Conexão ao banco de dados PostgreSQL
try:
    db = psycopg2.connect(
        host=os.getenv("DB_HOST", "dpg-cspqlnjv2p9s738u0560-a.oregon-postgres.render.com"),
        user=os.getenv("DB_USER", "instituto_apontar_user"),
        password=os.getenv("DB_PASSWORD", "NqD6qhYNIm0X9TJvLPlsBTlRUIKIKClR"),
        database=os.getenv("DB_NAME", "instituto_apontar"),
        port=os.getenv("DB_PORT", "5432")
    )
    cursor = db.cursor()
    print("Conexão com o banco de dados estabelecida com sucesso.")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit(1)

def get_last_synced_id():
    """
    Obtém o último ID sincronizado a partir da planilha.
    Presume que o ID está na primeira coluna da planilha.
    """
    rows = sheet.get_all_values()  # Recupera todas as linhas da planilha
    if len(rows) > 1:  # Verifica se há mais de uma linha (excluindo cabeçalhos)
        last_row = rows[-1]  # Obtém a última linha preenchida
        return int(last_row[0])  # Presume que o ID é a primeira coluna e é um número
    return 0  # Retorna 0 se a planilha estiver vazia (apenas cabeçalhos)

def get_unsynced_rows(last_synced_id):
    """
    Obtém as linhas do banco de dados com ID maior que o último ID sincronizado.
    """
    query = "SELECT * FROM acessos WHERE id > %s ORDER BY id ASC"
    cursor.execute(query, (last_synced_id,))
    rows = cursor.fetchall()

    # Processar as linhas
    unsynced_rows = []
    for row in rows:
        processed_row = [
            col.isoformat() if isinstance(col, datetime.datetime) else
            str(col) if isinstance(col, datetime.timedelta) else
            col
            for col in row
        ]
        unsynced_rows.append(processed_row)
    return unsynced_rows

def sync_db_to_sheet():
    """
    Sincroniza incrementalmente novas linhas do banco de dados para a planilha.
    """
    try:
        # Obter o último ID sincronizado
        last_synced_id = get_last_synced_id()
        print(f"Último ID sincronizado: {last_synced_id}")

        # Obter linhas não sincronizadas do banco de dados
        unsynced_rows = get_unsynced_rows(last_synced_id)
        print(f"Linhas não sincronizadas encontradas: {len(unsynced_rows)}")

        if unsynced_rows:
            for i, row in enumerate(unsynced_rows):
                print(f"Sincronizando linha {i + 1}: {row}")
                sheet.append_row(row)

            print("Novas linhas sincronizadas com sucesso.")
        else:
            print("Nenhuma nova linha para sincronizar.")
    except Exception as e:
        print(f"Erro ao sincronizar banco -> planilha: {e}")

# Loop para sincronização contínua
try:
    while True:
        print("Sincronizando banco de dados -> planilha...")
        sync_db_to_sheet()
        sleep(5)  # Espera 5 segundos antes de verificar novamente
except KeyboardInterrupt:
    print("Sincronização encerrada pelo usuário.")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    cursor.close()
    db.close()
