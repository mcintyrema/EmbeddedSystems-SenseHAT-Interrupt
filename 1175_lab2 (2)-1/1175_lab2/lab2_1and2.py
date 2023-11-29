from sense_hat import SenseHat
import time

sense = SenseHat()

# Task 1
#while True:
	#sense.show_message("Hello World")
	
#Task 2
r = (255, 0, 0)
o = (255, 127, 0)
y =(255, 255, 0)
g = (0, 255, 0)
b = (0,0,255)
bk = (0,0,0)
white = (255, 255, 255)
p = (75, 0, 130)
while True:
	for event in sense.stick.get_events():
		if event.direction == "right" and event.action == "held":
			sense.show_message("What's up?")
		elif event.direction == "middle" and event.action == "held":
			image = [b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,y,y,y,y,y,y,y,y,g,g,g,g,g,g,g,g,b,b,b,b,b,b,b,b
			,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,y,y,y,y,y,y,y,y,y]
			sense.set_pixels(image)
		elif event.direction == "left" and event.action == "released":
			temp = sense.get_temperature()
			temp = round(temp,1)
			message = "Temperature = {}".format(temp)
			sense.show_message(message)
		elif event.direction == "up" and event.action == "released":
			hum = sense.get_humidity()
			hum = round(hum,1)
			message = "Humidity = {}".format(hum)
			sense.show_message(message)
		elif event.direction == "down" and event.action == "released":
			pres = sense.get_pressure()
			pres = round(pres,1)
			message = "Pressure = {}".format(pres)
			sense.show_message(message)
