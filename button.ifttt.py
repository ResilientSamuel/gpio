from gpiozero import LED, Button
from signal import pause
import urllib2

led = LED(17)
button = Button(2)

def ifttt():
	urllib2.urlopen("https://maker.ifttt.com/trigger/button_pressed/with/key/m7J1Oo1PiH_mwczee6eRGSvAa9Lne4qQ1I5Q2k3J7gD")

button.when_pressed = ifttt

pause()

