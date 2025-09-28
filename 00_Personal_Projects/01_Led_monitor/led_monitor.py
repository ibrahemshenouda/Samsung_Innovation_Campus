import BlynkLib
import time
from gpiozero import LED, Device


blynk_auth = 'ymAmTaVIb2LDtAI_CxRRETFSKAz0Gqcj'
blynk = BlynkLib.Blynk(blynk_auth,server="blynk.cloud", port = 80)

red_led = LED(6)
yellow_led = LED(13)
green_led = LED(19)
white_led = LED(26)


def red_led_handler (value):
	if int(value[0]) ==  1:
		red_led.on()
	else:
		red_led.off()

def yellow_led_handler (value):
        if int(value[0]) == 1:
                yellow_led.on()
        else:
                yellow_led.off()

def green_led_handler (value):
        if int(value[0]) == 1:
                green_led.on()
        else:
                green_led.off()

def white_led_handler (value):
        if int(value[0]) == 1:
                white_led.on()
        else:
                white_led.off()




blynk.on("V0", red_led_handler)
blynk.on("V1", yellow_led_handler)
blynk.on("V2", green_led_handler)
blynk.on("V3", white_led_handler)

while True:
	blynk.run()
	time.sleep(0.1)
