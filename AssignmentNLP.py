#Run in version Python 2.7
#Speech to Text Recognition using Google Speech API

#This feels like the easiest Speech Recognition API out there atm
#It also has the ability to take in audio files and read them back to you
#This format basically finds your microphone and you speak into it
#Obviously I'm no expert and I don't know how to tweak this to the best settings
#Overall pretty good

#sudo pip install SpeechRecognition (Windows)

#sudo apt-get install python-pyaudio python3-pyaudio (Linux)

#pip install pyaudio

import speech_recognition as sr
 
#find the usb microphone name and enter it
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
#Sample rate
sample_rate = 48000
#Chunk is the buffer size
chunk_size = 2048
#Initializing the recognition
r = sr.Recognizer()
 
#list of microphone names
mic_list = sr.Microphone.list_microphone_names()
 
#loop to set device ID
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
 
#Using the mic for input and throwing an error if there is something wrong
with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                        chunk_size = chunk_size) as source:
    #lets recognizer adjust and sets the audio level
    print "Say Something"
    #user input (voice)
    audio = r.listen(source)
         
    try:
        text = r.recognize_google(audio)
        print "you said: " + text
     
    #error occurs when google could not understand what was said
     
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
     
    except sr.RequestError as e:
        print("Could not request results from Google 
                                 Speech Recognition service; {0}.format(e))
