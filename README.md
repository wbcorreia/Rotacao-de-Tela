# 🎛️ Controle de Rotação de Monitor com ESP32 WROOM + MPU6050 + Linux

Este projeto permite que um ESP32 com sensor MPU6050 controle a rotação de um monitor conectado a um computador com Linux, usando a leitura da orientação do sensor para girar automaticamente a tela.

## 🧰 Requisitos

### Hardware
- ESP32
- Sensor MPU6050 (acelerômetro/giroscópio)
- Cabo USB para conexão

### Software no ESP32
- MicroPython instalado no ESP32
- Biblioteca `mpu6050` , `pyserial`

### Software no PC (Linux)
- Python 3
- Pacotes:
  ```bash
  sudo apt install python3-serial python3-xlib x11-utils x11-xserver-utils
  ```

### 💻 PRÉ-REQUISITOS NO LINUX
1. Instalar dependências:
    ```
    sudo apt install python3-serial x11-xserver-utils
    ```
2. Permissões de acesso à porta serial (evita uso do sudo):
    ```
    sudo usermod -aG dialout $USER
    ```
(Depois reinicie a sessão ou o computador)

3. Verifique o nome da tela com:
    ```
    xrandr | grep -w connected
    ```
4. Torne o script executável, se desejar:
    ```
    chmod +x rotate_screen.py
    ```
5. Execute com:
    ```
    python3 rotate_screen.py
    ```
6. OBS: Teste a leitura da serial antes com:
    ```
    cat /dev/ttyUSB0
    ```


### 👨‍🔧 Contribuição
Melhorias são bem-vindas! Faça um fork e mande um pull request.\
Feito para automatizar e explorar o poder do Linux + MicroPython + sensores.
\
\
\
_Este projeto foi idealizado e desenvolvido com apoio do modelo de linguagem ChatGPT da OpenAI para geração de código, comentários explicativos e boas práticas._\
_Todas as decisões técnicas, testes e validações foram conduzidos manualmente, garantindo controle e responsabilidade sobre o conteúdo final._

