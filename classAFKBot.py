#!py -3.6
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 100)
phrases = {"hello" : "hello"}
def recognize(recognizer, microphone):

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("Unknown recognizer object")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("Unknown recognizer object")

    with microphone as src:
        recognizer.adjust_for_ambient_noise(src)
        audio = recognizer.listen(src)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Audio not recognised"

def generate_ans(inputwords):
    if inputwords in phrases.keys():
        return phrases[inputwords]
    else:
        return "Fuck you bitch imma finna pull out the 9"

def speakback(ans):
    engine.say(ans)
    engine.runAndWait()


r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=3)
print('ready...')

while True:
    detec = recognize(r, mic)
    print(detec)
    ans = generate_ans(detec)
    speakback(ans)