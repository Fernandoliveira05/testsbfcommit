

## Materiais utilizados para a primeira versão de protótipo 

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


