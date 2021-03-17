import RPi.GPIO as gpio
from time import sleep

#Configurar como modo BCM
gpio.setmode(gpio.BCM)

#Configura os leds como saída
gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.OUT)

#Aciona as saídas
gpio.output(17, gpio.LOW)
sleep(2)
gpio.output(27, gpio.LOW)
sleep(2)
gpio.output(17, gpio.HIGH)
gpio.output(27, gpio.HIGH)
#Desfaz modificações no GPIO
gpio.cleanup()
