import serial
import time
from datetime import datetime

# Substitua 'COM3' pelo nome da porta serial do seu Arduino
arduino = serial.Serial('/dev/cu.usbserial-1410', 9600)
time.sleep(2)  # Aguarda a conexão ser estabelecida

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")  # Formata a hora
    arduino.write(current_time.encode())  # Envia a hora para o Arduino
    arduino.write(b'\n')  # Envia uma nova linha
    time.sleep(1)  # Aguarda 1 segundo antes de enviar novamente
