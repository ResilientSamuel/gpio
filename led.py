from gpiozero import LED
from time import sleep

led = LED(17)

def dot():
	led.on()
	sleep(1)
	led.off()
	sleep(1)

def dash():
	
	
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
