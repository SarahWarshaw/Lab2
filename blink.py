import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

p = 25
f = 1
dc = 50

GPIO.setup(p, GPIO.OUT)

pwm = GPIO.PWM(p,f)

try:
  pwm.start(dc)
  while True:
    pass
except KeyboardInterrupt:
  print('\nExiting')

pwm.stop()
GPIO.cleanup()

