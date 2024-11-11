A proposta de solução IoT para o Instituto Apontar visa a criação de um sistema de controle de acesso seguro e eficiente, focado em melhorar a rotina e a segurança do ambiente. Este protótipo integra sensores biométricos, LEDs indicadores, buzzer e uma fechadura elétrica, todos coordenados pelo microcontrolador ESP32. O sistema permite autenticação por digital e cartão, com feedback sonoro e visual que garante uma experiência intuitiva e acessível para todos os usuários.

Cada componente foi selecionado para atender diretamente aos requisitos discutidos com o Instituto, incluindo acessibilidade e confiabilidade na operação. O protótipo utiliza um display LCD para exibir mensagens de status, LEDs que sinalizam estados específicos (como “Acesso Permitido” ou “Acesso Negado”), e um relé que controla o acionamento da fechadura elétrica de forma segura. O código, desenvolvido com nomes descritivos e funções modularizadas, garantindo uma estrutura de fácil manutenção para futuras implementações.

Essa primeira versão do protótipo físico demonstra o potencial da solução para otimizar a gestão de acesso no Instituto, contribuindo para um ambiente mais seguro, organizado e fácil de usar.

### Imagens do protótipo 

<div align="center">
  <sub>Figura X - Imagens Protótipo Inicial</sub><br>
  <img src="../prototipo_v1.0.gif" width="600px" height="auto">
  <br><sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

### Materiais utilizados para a primeira versão de protótipo 

Para a construção deste primeiro protótipo, foram empregados diversos componentes, cada um selecionado para possibilitar o funcionamento adequado do sistema e permitir testes iniciais das funcionalidades. Esses materiais incluem sensores para captura de dados, atuadores para respostas do sistema e módulos de controle, todos conectados ao microcontrolador ESP32, que gerencia as operações do protótipo.

| Material          | Especificação                              | Quantidade | Observações                                                    |
|-------------------|--------------------------------------------|------------|-----------------------------------------------------------------|
| ESP32            | Microcontrolador Wi-Fi e Bluetooth         | 1          | Controlador principal do sistema                               |
| Protoboard       | 830 pontos                                 | 3          | Para montagem do circuito e conexão dos componentes            |
| Leitor Biométrico DY50  | Sensor biométrico, interface UART | 1          | Para captura e verificação de digitais                           |
| LED vermelho              | 5mm, vermelho                              | 1          | Indicação visual de saída                                      |
| LED verde              | 5mm, verde                              | 1          | Indicação visual de entrada                                      |
| LED azul              | 5mm, azul                              | 1          | Indicação visual de funcionamento do sistema                                      |
| Resistor para LED Azul| 330Ω                                            | 1          | Limita corrente para LED azul                                  |
| Resistor para LED Verde | 220Ω                                          | 1          | Limita corrente para LED verde                                 |
| Resistor para LED Vermelho | 220Ω                                       | 1          | Limita corrente para LED vermelho                              |
| Jumpers          | Macho-Macho, Fêmea-Fêmea, Macho-Fêmea, várias cores                | Diversos   | Fios de conexão para protoboard                                |
| Fonte de Alimentação | 9V                                     | 1          | Fonte de alimentação dedicada para a fechadura, essencial para garantir seu funcionamento adequado, pois não operava apenas com a energia fornecida pelo circuito principal.   |
| Módulo Relé           | Relé de 5V para ESP32, suporta carga de 12V      | 1          | Permite que o ESP32 controle a fechadura elétrica de forma segura |
| Fechadura Elétrica    | Fechadura de 12V, ativada via relé               | 1          | Controlada pelo ESP32 através de um módulo relé para acionamento seguro |
| Buzzer                | Buzzer piezoelétrico 5V                          | 1          | Emite alertas sonoros em resposta a eventos                    |

### Conexões 

Para garantir o funcionamento adequado do protótipo, foi necessário realizar as conexões de forma cuidadosa e organizada entre o microcontrolador ESP32 e os demais componentes. Abaixo, detalhamos as conexões de cada elemento utilizado no protótipo.

| Componente           | Pino no ESP32   | Pino no Componente | Função/Descrição                                      |
|----------------------|-----------------|---------------------|-------------------------------------------------------|
| **Leitor Biométrico**| GPIO 16 (RX)    | TX                 | Comunicação Serial para leitura de digitais           |
|                      | GPIO 17 (TX)    | RX                 |                                                      |
| **LCD I2C**          | GPIO 21 (SDA)   | SDA                | Exibe mensagens de status                             |
|                      | GPIO 22 (SCL)   | SCL                | Endereço I2C padrão (0x27)                            |
| **LED Verde**        | GPIO 25         | Anodo (+)          | Indica acesso autorizado                              |
| **LED Azul**         | GPIO 33         | Anodo (+)          | Indica sistema em espera                              |
| **LED Vermelho**     | GPIO 32         | Anodo (+)          | Indica acesso negado                                  |
| **Buzzer**           | GPIO 26         | Pino positivo (+)    | Emite som para sinalização de acesso                  |
| **Relé (Fechadura)** | GPIO 18         | Pino de controle (IN)  | Acionamento da fechadura elétrica                     |

A alimentação dos dispositivos foi distribuída a partir das portas de energia do ESP32 (GND e 5V), conectadas à protoboard para fornecer energia de forma organizada a todos os componentes do circuito.

### Código Fonte do Protótipo

O código-fonte do protótipo foi desenvolvido para gerenciar os sensores, atuadores e o fluxo de dados entre os componentes conectados ao ESP32. Ele inclui funções para autenticação biométrica, controle de LEDs e relé, e feedback sonoro através do buzzer.

Para acessar o código completo e explorar sua implementação, [clique aqui para ver o arquivo completo.](src\protótipo\prototipo_v1.ino)

#### 1. Inicialização dos Componentes
Este bloco configura o ESP32 e os componentes conectados, como o LCD, leitor biométrico, LEDs, e buzzer. Essa etapa garante que todos os dispositivos estejam prontos para uso.

```cpp
void setup() {
    inicializarLCD();
    inicializarSerial();
    configurarPinos();
    verificarLeitorBiometrico();
}
```

* Funções chamadas:
  * inicializarLCD(): Inicializa o display LCD e exibe uma mensagem de inicialização.
  * inicializarSerial(): Configura a comunicação entre o ESP32 e o leitor biométrico.
  * configurarPinos(): Define os pinos dos LEDs, relé, e buzzer como saídas.
  * verificarLeitorBiometrico(): Verifica a conexão com o leitor biométrico e exibe o número de digitais registradas.
 
#### 2. Função para Captura e Identificação da Digital
A função capturarIdDigital() realiza a leitura da digital presente no sensor e tenta convertê-la para um ID válido. Ela verifica se há uma digital no sensor, converte a imagem para um template, e busca um ID correspondente. Em caso de sucesso, retorna o ID; caso contrário, indica que a digital não foi reconhecida.

```cpp
int capturarIdDigital() {
    uint8_t p = leitorBiometrico.getImage();
    if (p == FINGERPRINT_NOFINGER) return -1; // Nenhuma digital detectada
    else if (p != FINGERPRINT_OK) {
        Serial.println("Erro ao capturar imagem");
        return -1;
    }

    p = leitorBiometrico.image2Tz();
    if (p != FINGERPRINT_OK) {
        Serial.println("Erro ao converter imagem");
        return -1;
    }

    p = leitorBiometrico.fingerFastSearch();
    if (p == FINGERPRINT_OK) {
        Serial.print("ID encontrado: ");
        Serial.println(leitorBiometrico.fingerID);
        return leitorBiometrico.fingerID; // Retorna o ID encontrado
    } else {
        Serial.println("Digital nao encontrada");
        return -2; // Digital lida, mas sem correspondência
    }
}

```

* Processo:
  * Captura da imagem da digital.
  * Conversão da imagem para um template.
  * Pesquisa do template no banco de dados do sensor para encontrar um ID correspondente.



#### 3. Exibição de Mensagens e Controle de Acesso
Este bloco contém as funções exibirAcessoPermitido() e exibirAcessoNegado(), que exibem mensagens no LCD e acionam os LEDs e o buzzer conforme o resultado da verificação de digital. Elas são acionadas quando o acesso é permitido ou negado, proporcionando feedback visual e sonoro.

```cpp
void exibirAcessoPermitido() {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Acesso Permitido");
    tone(BUZZER_PIN, 1000, 200); // Emite tom curto no buzzer
}

void exibirAcessoNegado() {
    lcd.clear();
    lcd.setCursor(0, 0);
    tone(BUZZER_PIN, 500, 1000); // Emite tom longo no buzzer
    lcd.print("Acesso negado");
    delay(1000);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Tente Novamente!");
}
```

* Funções de Feedback:
  * exibirAcessoPermitido(): Exibe uma mensagem de "Acesso Permitido" e emite um tom curto.
  * exibirAcessoNegado(): Exibe uma mensagem de "Acesso Negado", emite um tom longo e pede para tentar novamente.


#### 4. Controle dos LEDs
As funções acenderLedVerde(), acenderLedVermelho(), gerenciarLedVerde() e gerenciarLedVermelho() controlam o tempo de ativação dos LEDs, permitindo que fiquem acesos apenas pelo tempo necessário.

```cpp
void acenderLedVerde() {
    digitalWrite(LED_VERDE, HIGH);
    digitalWrite(LED_AZUL, LOW);
    ledVerdeAceso = true;
    tempoLedVerde = millis(); // Marca o tempo atual para controle do tempo de acendimento
}

void acenderLedVermelho() {
    digitalWrite(LED_VERMELHO, HIGH);
    digitalWrite(LED_AZUL, LOW);
    ledVermelhoAceso = true;
    tempoLedVermelho = millis(); // Marca o tempo atual para controle do tempo de acendimento
}

void gerenciarLedVerde() {
    if (ledVerdeAceso && millis() - tempoLedVerde >= duracaoLedVerde) {
        digitalWrite(LED_VERDE, LOW);
        ledVerdeAceso = false;
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Instituto");
        lcd.setCursor(0, 1);
        lcd.print("Apontar");
        digitalWrite(LED_AZUL, HIGH); // Retorna ao estado de espera
    }
}

void gerenciarLedVermelho() {
    if (ledVermelhoAceso && millis() - tempoLedVermelho >= duracaoLedVermelho) {
        digitalWrite(LED_VERMELHO, LOW);
        ledVermelhoAceso = false;
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Instituto");
        lcd.setCursor(0, 1);
        lcd.print("Apontar");
        digitalWrite(LED_AZUL, HIGH); // Retorna ao estado de espera
    }
}
```
* Funções:
  * acenderLedVerde() e acenderLedVermelho(): Acendem os LEDs verde e vermelho, respectivamente, e registram o tempo em que foram ativados.
  * gerenciarLedVerde() e gerenciarLedVermelho(): Apagam os LEDs após o tempo especificado, voltando o sistema ao estado de espera.


 #### 5. Controle do Relé para Fechadura
O relé controla o acionamento da fechadura elétrica e é ativado por um tempo específico após a verificação de uma digital válida.

 ```cpp
void ativarRele() {
    digitalWrite(RELE_PIN, LOW); // Ativa a fechadura
    releAtivo = true;
    tempoAtivacaoRele = millis(); // Armazena o tempo de ativação
}

void desativarRele() {
    if (releAtivo && millis() - tempoAtivacaoRele >= 5000) {
        digitalWrite(RELE_PIN, HIGH); // Desativa a fechadura após 5 segundos
        releAtivo = false;
    }
}
 ```
* Funções de Controle:
  * ativarRele(): Liga o relé para acionar a fechadura e registra o tempo de ativação.
  * desativarRele(): Desliga o relé após 5 segundos, garantindo que a fechadura não fique ativa por tempo indeterminado.
