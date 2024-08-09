import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def recognize_speech() -> str:
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        return "Извините, я не понял, что вы сказали."
    except sr.RequestError as e:
        return f"Ошибка сервиса распознавания речи: {e}"


def speak(text: str):
    engine.say(text)
    engine.runAndWait()
