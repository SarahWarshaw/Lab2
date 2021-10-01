import RPi.GPIO as GPIO
from time import sleep

in1, in2 = 5, 26
LED1, LED2, LED3 = 25, 16, 21
f = 1
pin2LED = {in1:LED1, in2:LED2}
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

def myCallback(pin):
   pwm = GPIO.PWM(pin2LED.get(pin),f)
   try:
     pwm.start(0)
     for dc in range(101):
        pwm.ChangeDutyCycle(dc)
        sleep(0.005)
     for dc in range(101):
        pwm.ChangeDutyCycle(100-dc)
        sleep(0.005)
   except KeyboardInterrupt:
    print ('\nExiting')
   except Exception as e:
    print('\ne')
   pwm.stop()
   GPIO.cleanup()
  

GPIO.add_event_detect(in1, GPIO.RISING, callback = myCallback,bouncetime = 100)
GPIO.add_event_detect(in2, GPIO.RISING, callback = myCallback,bouncetime = 100)

try:
  while True:
    GPIO.output(LED3,0)
    sleep(0.5)
    GPIO.output(LED3,1)
    sleep(0.5)
except KeyboardInterrupt:
  print('\nExiting')
except Exception as e:
  print('\ne')

GPIO.cleanup()

