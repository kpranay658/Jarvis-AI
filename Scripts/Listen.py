import speech_recognition as sr
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, 0, 3)
    try: return r.recognize_google(audio).lower()
    except: return ""
