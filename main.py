import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
	tts = gTTS(text=text, Lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recongnize_google(audio)
			print(said)
		except: Exception as e:
			print("Exception: " + str(e))

	return said


text = get_audio

if "hello" in text:
	speak("hello, how are you Victor?")

if "what is your name" in text:
	speak("my name is DIDI i was created by Victor Peter")