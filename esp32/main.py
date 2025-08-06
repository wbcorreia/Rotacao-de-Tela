from machine import I2C, Pin
from mpu6050 import MPU6050
import time

# Inicializa I2C e o sensor
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
sensor = MPU6050(i2c)

def get_orientation():
    accel_data = sensor.read_accel_data()  # <-- Aqui está o método correto
    x = accel_data['x']
    y = accel_data['y']
    z = accel_data['z']

    # Simples lógica para "orientação"
    if abs(x) > abs(y):
        if x > 0:
            return "Landscape"
        else:
            return "Landscape (invertido)"
    else:
        if y > 0:
            return "Portrait"
        else:
            return "Portrait (invertido)"

while True:
    orientacao = get_orientation()
    print(orientacao)
    time.sleep(1)
