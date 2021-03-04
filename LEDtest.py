import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(18, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(25, gpio.OUT)

def ledTest():
    print "led on 1"
    gpio.output(18,gpio.HIGH)
    time.sleep(1)
    gpio.output(18,gpio.LOW)
    
    print "led on 2"
    gpio.output(23,gpio.HIGH)
    time.sleep(1)
    gpio.output(23,gpio.LOW)
    
    
    print "led on 3"
    gpio.output(24,gpio.HIGH)
    time.sleep(1)
    gpio.output(24,gpio.LOW)
    
    
    print "led on 4"
    gpio.output(25,gpio.HIGH)
    time.sleep(1)
    gpio.output(25,gpio.LOW)
    
    gpio.cleanup()

    
    


while True:
    init()
    ledTest()
    time.sleep(0.01)



