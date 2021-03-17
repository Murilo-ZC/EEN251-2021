import RPi.GPIO as gpio
from time import sleep

#Configurar como modo BCM
gpio.setmode(gpio.BCM)

#Configura os leds como saída
gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.IN, pull_up_down= gpio.PUD_UP)

#Aciona as saídas
try:
    while True:
        if(gpio.input(22) == 0):
            gpio.output(17, gpio.LOW)
            gpio.output(27, gpio.HIGH)
        else:
            gpio.output(17, gpio.HIGH)
            gpio.output(27, gpio.LOW)
except:
    #Desfaz modificações no GPIO
    gpio.cleanup()
#Termina a execução
exit()
