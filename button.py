from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)

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


button.when_pressed = dash
button.when_released = led.off

pause()

dot()
dash()
