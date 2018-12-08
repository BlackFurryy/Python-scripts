import speech_recognition as sr

r = sr.Recognizer()

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

with sr.Microphone() as source:
   print ('Speak Up')
   audio = r.listen(source)
   
   try:
       text	= r.recognize_google(audio)
       print('Did you said: {}'.format(text))
   except:
       print('Did not get that')