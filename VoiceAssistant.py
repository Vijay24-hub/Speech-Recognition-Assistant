"""
@author: Vijay
"""
"""
Using python 
Created Speech recognition assistant 
and add basic features to it like 
searching on Google, Wikipedia search, shutdown and restart your pc etc.
"""
#importing packages
# text-to-speech
#speech recognizing
import pyttsx3
import speech_recognition as sr 
import datetime 
import random
import os
import pyjokes
import wikipedia
import webbrowser as wb

#initializing pyttsx3(text-to-speech)
engine=pyttsx3.init()
voices=engine.getProperty("voices")
#Changing voices
#voice[0]-boy voice
#voice[1]-girl voice
engine.setProperty('voice',voices[1].id)
#setting voice rate(speed of speech)
newVoiceRate=120
engine.setProperty('rate',newVoiceRate)
#setting volume 
Volume=1.0
engine.setProperty('volume',Volume)

#text-to-speech function
def speech(text):
    engine.say(text)
    engine.runAndWait()

#time function
def time():
    Time=datetime.datetime.now().strftime('%I:%M:%p')
    speech(Time)

#date function
def date():
    year=int(datetime.datetime.now().year)
    month=datetime.datetime.now().strftime('%B')
    date=int(datetime.datetime.now().day)
    speech('Current date is')
    speech(date)
    speech(month)
    speech(year)

#greeting function
def wishme():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speech('Good morning')
    elif hour>=12 and hour<18:
        speech('Good afternoon')
    elif hour>=18 and hour<21:
        speech('Good evening')
    else:
        speech('Good night')
    speech('Hello buddy Welcome back')
"""
def chrome():
    chrome_path="C:\Program Files\Google\Chrome\Application %s"
    search=takecommand().lower()
    wb.get(chrome_path).open_new_tab(search+'.com')
"""
#story telling function
def short_story():
    when = ["A few years ago", "Once upon a time", "Yesterday", "A long time ago", "One night", "One morning"]
    who = ["a lion", "a king", "an elephant", "a rat", "a boy", "a girl"]
    name = ["dobby", "Simba", "Mufasa", "Scooby", "Remy", "Nobi"]
    place = ["village", "forest", "river", "mountain", "space", "house"]
    went = ["school", "theatre", "party", "shopping"]
    happened = ["made a lot of friends", "Eats a lunch", "found a secret key", "solved a mistery case", "sings a song"]
    story = random.choice(when)+", "+random.choice(who)+" named as "+random.choice(name)+" that lived in "+random.choice(place)+", went to the "+random.choice(went)+" and "+random.choice(happened)
    print(story)
    speech(story)

#joke telling funtion
def jokes():
    joke=pyjokes.get_joke()
    print(joke)
    speech(joke)

#taking command from the user
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  #noise cancellation  
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio)
    except sr.UnknownValueError:
        print('sorry, I did not get that')
        return ''
    except sr.RequestError as e:
        print('sorry, my speech server is down')
        return ''
    return query

#main function
if __name__=='__main__':
    wishme()
    while True:
        command=takecommand()
        query=command.lower()
        print(query)
        if 'hello' in query:
            hello='hi, how can i help?'
            print(hello)
            speech(hello)
        elif 'what is your name' in query:
            name='Hi, I am your friend , you can call me to your wish'
            print(name)
            speech(name)
        elif 'who are you' in query:
            who='I am your speech recognition assistant, how can i help you'
            print(who)
            speech(who)
        elif 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'story' in query:
            short_story()
        elif 'signout' in query:
            os.system('shutdown - l')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        elif 'chrome search' in query:
            speech('What should I search?')
            chromepath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")
        elif 'joke' in query:
            jokes()
        elif 'wikipedia' in query:
            speech('searching')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speech(result)           
        elif 'bye' in query:
            speech('bye, see you')
            quit()
        else:
            print("try to say something")
            speech("try to say something")
            print("-current time")
            print()
            print("-current date")
            print()
            print("-short story teller")
            print()
            print("-Tell me a joke")
            print()
            print("wikipedia search")
        
