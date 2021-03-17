# Declara-se as bibliotecas que serão utilizadas no código
import RPi.GPIO as gpio
import time
import serial
 
#Configura o uso do terminal serial e da taxa de transmissão de dados
ser = serial.Serial("/dev/ttyS0", 9600)
 
gpio.setmode(gpio.BCM)

try:
 while True:
   
   ser.write("Enviando dados")
   print("aqui")
   time.sleep(2)
   data = []
   while(ser.available()>0):
    data.append(ser.read())
   print("Dados Recebidos:" + data)
   time.sleep(2)
except:
 gpio.cleanup()
exit()
