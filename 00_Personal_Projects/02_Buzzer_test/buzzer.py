import RPi.GPIO as GPIO
import time

buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)


try:
    while True:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(0.1) 
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
