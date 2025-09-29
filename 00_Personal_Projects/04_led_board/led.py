import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
PINS_BOARD = [31, 33, 35, 37]

for p in PINS_BOARD:
	GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)

while True:
	for p in PINS_BOARD:
            	GPIO.output(p, GPIO.HIGH)
            	time.sleep(1)
            	GPIO.output(p, GPIO.LOW)
            	time.sleep(0.5)
