#Objetivo do programa: Piscar um LED no pino 27
#E observar quando a entrada 22 for acionada

import RPi.GPIO as gpio
import time

PINO_ENTRADA = 22 

def rotina_interrupcao(pino):
    print("Entrou na interrupcao!")
    print("Quinta temporada logo ai!")

#Configurao da placa
gpio.setmode(gpio.BCM) #Configura para o pino do GPIO
gpio.setup(27, gpio.OUT) #Configura GPIO27 como saida
#Configura GPIO22 como entrada com pullup interno
gpio.setup(PINO_ENTRADA, gpio.IN, pull_up_down=gpio.PUD_UP)

#Configura a interrupção no pino de entrada
gpio.add_event_detect(PINO_ENTRADA, gpio.RISING, callback=rotina_interrupcao, bouncetime=300)

#rotina principal
try:
    while True:
        gpio.output(27, gpio.HIGH) #Desliga o LED
        time.sleep(2)
        gpio.output(27, gpio.LOW) #Liga o LED
        time.sleep(2)
except:
    gpio.cleanup()
exit()


