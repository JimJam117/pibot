import RPi.GPIO as gpio
import time

### My Basic Robot Movement Functions ###
## by jimjam 04 March 2021

# Init - set all the pins we'll use 
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)


# pivots on the spot, turning one wheel in reverse and one forwards

def pivot_left(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

# turns by just making one wheel go forwards

def turn_left(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

# raw forwards and backwards without any adjustment

def forward(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def backward(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


# Same as regular forward/backward, but corrected for the left and right motors

def forwardPwm(tf, left_motor_in, right_motor_in):
    init()
    right_motor = gpio.PWM(13, 100)
    right_motor.start(right_motor_in)

    left_motor = gpio.PWM(7, 100)
    left_motor.start(left_motor_in)

    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def backwardPwm(tf, left_motor_in, right_motor_in):
    init()

    right_motor = gpio.PWM(11, 100)
    right_motor.start(right_motor_in)

    left_motor = gpio.PWM(15, 100)
    left_motor.start(left_motor_in)

    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


### Testing Variables ###

#go time
gt = 2
#sleep time
st = 1
