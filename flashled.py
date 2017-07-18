from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)

def dot():
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.1)

def dash():
	led.on()
	sleep(1)
	led.off()
	sleep(1)

def R():
	dot()
	dash()
	dash()

def E():
	dot()
	
def S():
	dot()
	dot()
	dot()

def I():
	dot()
	dot()

def say_my_name():
	R()
	E()
	S()
	I()
	

button.when_pressed=say_my_name
pause()
