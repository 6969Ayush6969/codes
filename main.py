import speech_recognition as sr
import pyaudio
import pyttsx3
import webbrowser
from songsplaylist import playlists,songs


# tasks
def work(text):
            if 'youtube' in text.lower():
                if 'search' in text.lower():
                    webbrowser.open(f'https://www.youtube.com/results?search_query={spl[-1]}')
                else:
                    webbrowser.open('https://www.youtube.com')
            elif 'instagram' in text.lower():
                webbrowser.open('https://www.instagram.com')
            elif 'playlist' or 'playlists' in spl:
                 try:
                     for index,elem in enumerate(spl):
                         if elem in playlists.keys():
                           webbrowser.open(playlists[elem])
                 except:
                     speak(f'cant find {AtT1}')
            elif 'song' in text.lower():
                try:
                 for index,elem in enumerate(spl):
                    print(elem)
                    if elem in songs.keys():
                     webbrowser.open(songs[elem])
                except Exception as e:
                    speak(f'Cant find the song')
                    
# jarvis
if __name__=='__main__':
    # this will speak only
    def speak(command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command) 
        engine.runAndWait()
    speak('Jarvis bhhai ready...')
    
    # listening audio
    while True:
        r = sr.Recognizer()
        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                print('Loading...')
            AtT=r.recognize_google(audio) #AtT= Audio to text
            print(AtT)
            if (AtT.lower()=='jarvis'):
                speak('yes')
                with sr.Microphone() as source:
                 print("Jarvis Listening...")
                 audio = r.listen(source)
                 print('Loading...')
                AtT1=r.recognize_google(audio)
                spl=AtT1.split(' ')
                print(spl)
                work(AtT1)
            elif (AtT.lower()=='break') or (AtT.lower()=='finish') or (AtT.lower()=='end') :
                speak('Bravo going dark!')
                break
            else:
                pass 
        except Exception as e:
            print('Error!')
            
        