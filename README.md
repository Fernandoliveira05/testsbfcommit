A proposta de solução IoT para otimizar o dia a dia do Instituto Apontar é uma estrutura completa e integrada, desenvolvida para atender as necessidades específicas do instituto. Esta solução reúne sensores, microcontroladores e atuadores, todos coordenados por um código bem documentado e intuitivo, para facilitar futuras manutenções. A primeira versão física do protótipo foi projetada para cumprir todos os requisitos definidos pelo Instituto, com atenção especial aos aspectos de acessibilidade discutidos anteriormente com o instituto. O objetivo é criar um sistema que não apenas agilize os processos, mas também ofereça segurança e facilidade de uso, proporcionando uma experiência mais eficiente e tranquila para todos no Instituto.

## Imagens do protótipo 

<div align="center">
  <sub>Figura X - StoryBoard com Solução Implementada</sub><br>
  <img src="../assets/storyboard1.png" width="600px" height="auto">
  <br><sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura X - StoryBoard com Solução Implementada</sub><br>
  <img src="../assets/storyboard1.png" width="600px" height="auto">
  <br><sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura X - StoryBoard com Solução Implementada</sub><br>
  <img src="../assets/storyboard1.png" width="600px" height="auto">
  <br><sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura X - StoryBoard com Solução Implementada</sub><br>
  <img src="../assets/storyboard1.png" width="600px" height="auto">
  <br><sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>

## Materiais utilizados para a primeira versão de protótipo 

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

## Conexões 

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

## Código para funcionamento do protótipo

O código-fonte do protótipo foi desenvolvido para gerenciar os sensores, atuadores e o fluxo de dados entre os componentes conectados ao ESP32. Ele inclui funções para autenticação biométrica, controle de LEDs e relé, e feedback sonoro através do buzzer.

Para acessar o código completo e explorar sua implementação, clique [aqui para ver o arquivo completo](src\protótipo\MUDAR)
