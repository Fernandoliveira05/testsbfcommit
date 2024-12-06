Nesta seção, apresentamos um **Diagrama de Sequência UML** que ilustra detalhadamente as interações entre os componentes do sistema em um cenário específico. Esse diagrama destaca o fluxo de mensagens e as ações realizadas pelos diferentes elementos, como o ESP32, broker MQTT, servidor web e banco de dados, ao atender a uma requisição de cadastro de digital. O protótipo físico apresentado nesta seção representa a integração de hardware e software em uma solução conectada via Wi-Fi e comunicação MQTT. Este protótipo foi projetado para validar o funcionamento completo do sistema em um ambiente conectado, permitindo o registro e monitoramento remoto de eventos, especificamente autenticações biométricas, além de fornecer feedback visual e sonoro em tempo real.

Os diagramas foram desenvolvidos com o objetivo de alinhar as funcionalidades da aplicação às necessidades dos usuários e stakeholders, evidenciando tanto o fluxo das operações quanto os estados e comportamentos do sistema. No contexto de sistemas IoT (Internet das Coisas), onde a comunicação e a integração entre dispositivos desempenham um papel central, essas representações visuais são ferramentas úteis para compreender e validar as diferentes camadas da solução.

Os Diagramas de Sequência UML cumprem um papel fundamental ao:
- **Demonstrar as interações entre componentes**: Facilitam a visualização da comunicação e colaboração entre diferentes elementos do sistema.
- **Fluxo de dados**: Detalham a troca de mensagens e respostas ao longo do tempo, permitindo identificar dependências e otimizar o desempenho.

Essa abordagem fornece aos desenvolvedores e gestores uma visão completa da solução, conectando a experiência do usuário (UX) ao funcionamento técnico e operacional do sistema. A seguir, exploramos detalhadamente cada diagrama, explicando como ele reflete a arquitetura e os fluxos de trabalho do projeto.

<div align="center">
  <sub>Figura X - Diagrama UML - Fluxo de Cadastro de Digital</sub><br>
  <img src="image.png" width="600px" height="auto"><br>
  <sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

# Registro de Situações de Uso

| **#** | **Configuração do Ambiente**                                                                                     | **Ação do Usuário**                                                                                             | **Resposta Esperada do Sistema**                                                                                                     | **Resposta Recebida do Sistema**                                                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01    | O ESP32 realiza a conexão inicial com o broker MQTT. O sensor biométrico e o LCD ficam disponíveis aguardando o início do cadastro. | Colocar o dedo no sensor biométrico para iniciar o cadastro.                                                    | O sensor biométrico lê a digital e exibe no LCD: **"Cadastrar: Nome, ID"**.                                                          | O sensor leu a digital com sucesso e o LCD exibiu a mensagem de progresso no cadastro.                                                                                               |
| 02    | O ESP32, conectado ao broker MQTT, publica os dados capturados pelo sensor biométrico para o servidor web.        | Realizar o cadastro no ESP32 para enviar a digital ao servidor.                                                 | O ESP32 envia os dados ao servidor, que os registra no banco de dados, retornando a mensagem de sucesso exibida no LCD: **"Sucesso"**. | O ESP32 publicou os dados corretamente, o servidor confirmou o cadastro, e o LCD exibiu a mensagem esperada.                                                                         |
| 03    | O servidor web interage com o banco de dados PostgreSQL, processando as solicitações do ESP32 e retornando respostas. | Solicitar uma autenticação biométrica no sistema colocando o dedo no sensor.                                    | O ESP32 valida a digital, acende o LED verde, exibe no LCD **"Acesso Permitido"**, e aciona o relé para liberar a fechadura.         | A autenticação foi realizada com sucesso: LED verde aceso, mensagem de permissão exibida no LCD, e o relé ativado corretamente.                                                       |
| 04    | O ESP32 tenta se reconectar automaticamente ao broker MQTT após uma perda de conexão.                            | Reiniciar o sistema para simular perda de conexão Wi-Fi e tentar acessar o sistema.                              | O ESP32 exibe no LCD: **"Erro na Conexão"**, tenta reconectar a cada 5 segundos e, após o sucesso, retorna ao estado normal.          | O ESP32 detectou a perda de conexão, exibiu a mensagem de erro no LCD, tentou reconectar, e restabeleceu a comunicação com o broker MQTT após algumas tentativas.                       |
| 05    | Configuração do sensor biométrico para verificar duplicidade local antes de enviar a digital ao servidor.         | Tentar cadastrar uma digital já registrada no sistema.                                                          | O ESP32 exibe no LCD: **"Dedo já cadastrado"** e interrompe o processo de cadastro.                                                  | A verificação local detectou duplicidade, exibindo corretamente a mensagem no LCD e encerrando o fluxo.                                                                              |
| 06    | O servidor Flask recebe e processa comandos enviados via MQTT.                                                   | Enviar uma solicitação de remoção de digital cadastrada pelo tópico MQTT **"instituto/remocao/biometrico"**.     | O servidor remove o ID correspondente do banco de dados e retorna uma mensagem de sucesso ao ESP32.                                 | O ID foi removido com sucesso do banco de dados, e a mensagem de confirmação foi recebida e exibida no LCD do ESP32.                                                                 |
| 07    | Uso do broker MQTT para enviar alertas de falha ao servidor e ao painel de monitoramento.                         | Simular uma falha no sensor biométrico durante o processo de leitura da digital.                                 | O ESP32 publica no tópico **"instituto/erro/sensor"** indicando a falha, e o servidor exibe um alerta no dashboard de monitoramento. | A falha foi corretamente detectada e publicada no tópico MQTT, com o painel de monitoramento exibindo um alerta visual correspondente à falha do sensor.                             |

---


### Configuração do Ambiente**

Para realizar os testes descritos, o ambiente deve estar configurado da seguinte forma:

#### **Hardware**
- **ESP32**: Microcontrolador central responsável pela comunicação com sensores e o broker MQTT.
- **Sensor Biométrico (DY50)**: Captura impressões digitais para autenticação e cadastro.
- **Leitor RFID**: Identifica usuários por meio de cartões RFID.
- **Relé**: Controla a abertura de fechaduras eletrônicas.
- **LEDs**:
  - Verde: Indica sucesso em autenticação ou cadastro.
  - Vermelho: Indica falha na autenticação ou cadastro.
- **Buzzer**: Emite sinais sonoros como feedback adicional.
- **Display LCD (I2C)**: Exibe mensagens em tempo real para o usuário, como "Acesso Permitido", "Acesso Negado" e "Erro no Cadastro".

### **Software**
- **Conexão Wi-Fi**: Configurada para conectar o ESP32 ao broker MQTT.
- **Broker MQTT (HiveMQ Cloud)**:
  - Centraliza a comunicação de eventos, registrando mensagens enviadas pelo protótipo.
  - Tópicos configurados:
    - `instituto/cadastro/usuario`
    - `instituto/cadastro/resposta`
    - `instituto/acesso/biometrico`
    - `instituto/remocao/biometrico`
- **Servidor Web (Flask)**:
  - Recebe os dados publicados pelo ESP32 via MQTT.
  - Processa e registra as informações no banco de dados.

---

## **2. Fluxo de Cadastro de Impressão Digital**

### **Descrição do Cenário**
O administrador realiza o cadastro de uma nova impressão digital no sistema. O sensor biométrico captura a digital, e o ESP32 verifica sua validade antes de enviá-la ao servidor para registro. O sistema fornece feedback visual e sonoro ao usuário.

### **Exemplo de Ação do Usuário e Resposta do Sistema**

| **Ação do Usuário**                          | **Resposta do Sistema**                                                                                  |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Usuário inicia o cadastro no ESP32.          | ESP32 exibe no LCD: **"Cadastrar:"**.                                                                    |
| Usuário coloca o dedo no sensor.             | Sensor DY50 captura a digital e envia os dados ao ESP32.                                                 |
| Digital já cadastrada.                       | ESP32 exibe no LCD: **"Dedo já cadastrado"**, encerra o fluxo.                                            |
| Digital não cadastrada.                      | ESP32 publica no tópico MQTT: **"instituto/cadastro/usuario"** com o ID biométrico.                      |
| Servidor processa e registra os dados.       | Banco de dados armazena a digital; servidor retorna sucesso no tópico: **"instituto/cadastro/resposta"**. |
| Feedback final para o usuário.               | ESP32 exibe no LCD: **"Sucesso"**, LED verde acende e buzzer emite um som breve.                          |

### **Diagrama de Sequência UML**

![Diagrama de Sequência UML - Fluxo de Cadastro de Impressão Digital](./diagrama_cadastro_digital.png)

---

## **3. Fluxo de Autenticação Biométrica**

### **Descrição do Cenário**
Um usuário autenticado utiliza o sistema para liberar acesso. O sensor biométrico verifica a digital e o ESP32 consulta a base de dados via servidor para confirmar a autenticação.

### **Exemplo de Ação do Usuário e Resposta do Sistema**

| **Ação do Usuário**                          | **Resposta do Sistema**                                                                                  |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Usuário coloca o dedo no sensor.             | Sensor DY50 captura a digital e envia os dados ao ESP32.                                                 |
| Digital não encontrada no sistema.           | ESP32 exibe no LCD: **"Acesso Negado"**, acende o LED vermelho e o buzzer emite um som longo.             |
| Digital encontrada e validada.               | ESP32 publica no tópico MQTT: **"instituto/acesso/biometrico"** e aguarda resposta do servidor.           |
| Servidor confirma autenticação.              | Banco de dados valida o acesso e retorna sucesso no tópico: **"instituto/acesso/biometrico/resposta"**.   |
| Feedback final para o usuário.               | ESP32 exibe no LCD: **"Acesso Permitido"**, LED verde acende e relé libera a fechadura.                   |

### **Diagrama de Sequência UML**

![Diagrama de Sequência UML - Fluxo de Autenticação Biométrica](./diagrama_autenticacao_biometrica.png)

---

## **4. Casos de Falha**

### **Cenário 1: Falha na Conexão Wi-Fi**
| **Ação do Usuário**                          | **Resposta do Sistema**                                                                                  |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Usuário tenta realizar o cadastro ou acesso. | ESP32 tenta conectar ao broker MQTT, mas falha.                                                         |
| Falha na conexão Wi-Fi.                      | ESP32 exibe no LCD: **"Erro na Conexão"**, e repete a tentativa a cada 5 segundos até reconectar.         |

---

## **5. Testes e Validação**

| **Situação de Teste**                        | **Critério de Sucesso**                                                                                  |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Cadastro de digital não duplicada.           | Digital é registrada no banco de dados, feedback no LCD exibe "Sucesso".                                 |
| Cadastro de digital duplicada.               | ESP32 exibe no LCD: "Dedo já cadastrado" e encerra o fluxo.                                              |
| Autenticação de digital válida.              | LED verde acende, relé libera a fechadura, e o LCD exibe "Acesso Permitido".                             |
| Autenticação de digital inválida.            | LED vermelho acende, buzzer emite som longo, e o LCD exibe "Acesso Negado".                              |
| Perda de conexão com o servidor.             | ESP32 tenta reconectar ao broker MQTT automaticamente e exibe "Erro na Conexão".                        |

---


