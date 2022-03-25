import speech_recognition
import pyaudio
import pyttsx3
from datetime import date
from datetime import datetime
import requests, json

def weather(city_name):
	api_key ="18db6e4be0669ea2952244e9a19e8279"
	base_url ="http://api.openweathermap.org/data/2.5/weather?"
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	response = requests.get(complete_url)
	x = response.json()
	if x["cod"] != "404":
		y = x["main"]
		current_temperature = int(y["temp"] - 273.15) 
		current_pressure = y["pressure"]
		current_humidity = y["humidity"]
		z = x["weather"]
		weather_description = z[0]["description"]
		robot_brain = "Current: " + str(weather_description) + ", Temperature is " + str(current_temperature) + "°С, " + "Humidity is " + str(current_humidity) + "%"
	else:
		robot_brain = "Can not find the city"
	return robot_brain

def listenen():
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic, timeout=3, phrase_time_limit=5)
		print("Robot: ...") 
	try:
	    you1 = robot_ear.recognize_google(audio, language='en')
	    print(you1)		
	except:
		print('')

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


while True:
	with speech_recognition.Microphone() as mic:
	    print("Robot: I'm listening")
	    audio = robot_ear.listen(mic, timeout=3, phrase_time_limit=3)
	print("Robot: ...")

	try:
	    you = robot_ear.recognize_google(audio)
	except:
	    you = ""
	print("You: " + you)

	if you =="":
	    robot_brain = "I can't hear you"
	elif "hello" in you:
	    robot_brain = "hello Duy"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S second")
	elif "temperature" in you:
		robot_brain = "Your city name"
		print("Robot: " + robot_brain)
		you1 = listenen()
		print("You search: " + you)
		if "Didn't find the city name" in robot_brain:
			you = input("Robot: Try input: ")
			robot_brain = weather(you)
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break	
	elif "bye" in you:
		robot_brain = "Bye Duy"
		print("Robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
	    robot_brain ="I'm fine thank you"
	    
	print("Robot: " + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()