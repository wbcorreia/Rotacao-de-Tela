import serial
import subprocess
import time
import os

# Configure aqui seu monitor e porta
MONITOR = "HDMI-1"
PORTA = "/dev/ttyUSB0"
BAUDRATE = 115200

# Define display para ambiente gráfico
os.environ["DISPLAY"] = ":0"

def rotate_screen(orientation):
    rotations = {
        "Landscape": "normal",
        "Landscape (invertido)": "inverted",
        "Portrait": "left",
        "Portrait (invertido)": "right"
    }
    rotation = rotations.get(orientation.strip())
    if rotation:
        subprocess.run(["xrandr", "--output", MONITOR, "--rotate", rotation])
        print(f"Tela girada para {rotation}")

def main():
    try:
        ser = serial.Serial(PORTA, BAUDRATE, timeout=1)
    except Exception as e:
        print(f"Erro abrindo porta serial: {e}")
        return

    print("Esperando dados do ESP32...")

    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Recebido: {line}")
                rotate_screen(line)
        except Exception as e:
            print(f"Erro lendo serial: {e}")
        time.sleep(0.1)

if __name__ == "__main__":
    main()

done
