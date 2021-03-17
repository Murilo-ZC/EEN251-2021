#! /usr/bin/python
# -*- coding: utf-8 -*- 
import RPi.GPIO as gpio
#import RPIO
import time
def rotina_interrupcao(gpio_pin):
    print("Entrou na Interrupcao")
gpio.setmode(gpio.BCM)
gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.add_event_detect(22, gpio.BOTH, callback=rotina_interrupcao, bouncetime=300)
try:
    while True:
      gpio.output(27, gpio.HIGH)
      time.sleep(2)
      gpio.output(27, gpio.LOW)
      time.sleep(2)
except:
    gpio.cleanup()
exit()