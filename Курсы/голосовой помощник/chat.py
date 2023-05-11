import random
import os
import speech_recognition as sr
from gtts import gTTS
import playsound
import pyaudio

# Слушает и преобразовывает нашу речь
def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
        print(f"Вы сказали: {voice_text}")

        return voice_text
    except sr.UnknownValueError:
        return "Ошибка распознания"
    except sr.RequestError:
        return "Ошибка запроса"



# Обрабатывает команду 
def handle_command(command):
    if command == "Привет":
        say("Привет-привет")
        playsound.playsound(audio_3558.mp3)
    elif command == "пока":
        playsound.playsound(audio_4722.mp3)
        stop()
    else:
        playsound.playsound(audio_1064.mp3)
        say("Не понятно, повторите")

# Останавливает программу
def stop():
    say("До скорого")
    exit()

# Запускает программу 
def start():
    print("Запуск ассистента")

    while True:
        command = listen()
        handle_command(command)

# Безопасный запуск программы, в случае ошибки запуск прерывается 
try:
    start()
except KeyboardInterrupt:
    stop()
