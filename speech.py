import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        #print(text)
        print('You said: {0}'.format(text[0].upper()) + text[1:] + '.')

    except:
        print("Sorry, could not recognize your voice")
