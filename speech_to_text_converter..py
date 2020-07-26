import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak now...")
    r.adjust_for_ambient_noise(source, duration=10)
    audio=r.listen(source)
    print(r.recognize_google(audio))
