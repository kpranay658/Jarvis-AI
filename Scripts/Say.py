import pyttsx3
def Say(audio):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.say(audio)
    engine.runAndWait()
