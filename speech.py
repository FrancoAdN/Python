import speech_recognition as sr
loop = True
while loop:
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print ('Say Something!')
        audio = r.listen(source)
        #print ('Done!')
    try:
        text = r.recognize_google(audio)
        if text == 'false':
            print('here')
            loop = False
        else:
            print (text)
    except Exception as e:
        print(e)
