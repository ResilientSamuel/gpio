from gpiozero import LED
from time import sleep

led = LED(17)


def dot():
	led.on()
	sleep(1)
	led.off()
	sleep(1)

def dash():
	 led.on()
	 sleep(2)
	 led.off()
	 sleep(2)
      
dot()
dash()
dot()

