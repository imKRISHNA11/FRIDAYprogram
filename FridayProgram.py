import pyttsx3 as tts
import speech_recognition as sr
import webbrowser as wb
import datetime as dt
import os as os
import random as rd
from AppOpener import run
import pyautogui as pg
import time as td
import playsound as ps

#engine for tts
engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



#speak and audio function
def speak (audio):
    engine.say(audio)
    print("FRIDAY:",audio)
    engine.runAndWait()

#VoiceSpeed of tts
voicespeed = 180
engine.setProperty('rate',voicespeed)


#greeting function according real time
def greetMe():
    hour = dt.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

#speaking time function
def time():
    hour = dt.datetime.now().hour
    strTime = dt.datetime.now().strftime("%H:%M:%S")
    if hour > 0 and hour < 12:
        speak(f"Sir it's {strTime} A M")
    else:
        speak(f"Sir it's {strTime} P M")



#TakeCommand Function for Voice Input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
#        ps.playsound("C:\\Users\\home\\Desktop\\codes\\FRIDAY\\sound\\Listening sfx.mp3")
        print("\nListening....")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=4)  

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")

    except Exception as e:
        print("Plese try again...")
        return "None"
    return query 

#Function For Asking Name
def username():
    speak("What should i call you ?")
    username = takeCommand()
    #speak(f"\nHello {username}")
    print()
    speak(f"What can i help you {username} sir")  

def fav_playlist():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    speak("Opening your favourite music playlist on Youtube !")
    wb.get(chrome_path).open_new_tab("https://www.youtube.com/playlist?list=PLjQAbgoWTIATbz2oiUatrjjYpzF7PZjA7")
    speak("Which song should i play first sir ?")
    query = takeCommand().lower()
    if "first" in query or "Industry baby" in query :
        speak("Okay Sir Enjoy the music !")
        wb.get(chrome_path).open("https://www.youtube.com/watch?v=fx4SUZqg8CY&list=PLjQAbgoWTIATbz2oiUatrjjYpzF7PZjA7&index=1&ab_channel=Sush%26YohanMusic")
    elif "second" in query or "hikaru nara" in query:
        speak("Oaky Sir Enjoy the music !")
        wb.get(chrome_path).open("https://www.youtube.com/watch?v=p5kc8hJ3GcA&list=PLjQAbgoWTIATbz2oiUatrjjYpzF7PZjA7&index=2&ab_channel=BraveboyzzStudioOfficial")
    elif "third" in query or "tum kyu" in query :
        speak("Okay Sir Enjoy the music !")
        wb.get(chrome_path).open("https://www.youtube.com/watch?v=K6aIpWOJCmI&list=PLjQAbgoWTIATbz2oiUatrjjYpzF7PZjA7&index=3&ab_channel=VickySingh-Topic")
    elif "fourth" in query or "tum prem" in query :
        speak("Okay Sir Enjoy youe music !")
        wb.get(chrome_path).open("https://www.youtube.com/watch?v=BSGKR1IhFoQ&list=PLjQAbgoWTIATbz2oiUatrjjYpzF7PZjA7&index=4&ab_channel=MOhitLalwani")
    else:
        speak("Playing from number 1 ! Enjoy the music ! ")
        wb.get(chrome_path).open_new_tab("https://www.youtube.com/playlist?list=PLjQAbgoWTIATbz2oiUatrjjYpzF7PZjA7")
            


#Function for SimpleTalk
def talk():
    msg = rd.randint(0,3) #random message using random number and if..else 
    if(msg == 0):
        hour = dt.datetime.now().hour #message according real time
        if(hour < 12):
            speak("I am fine Sir ! Thanks for your concern ! How about you ! Sir Have you ate you breakfast ? ")
            query = takeCommand().lower()
        elif(hour > 12) and (hour < 16):
            speak("I am fine Sir ! Thanks for your concern ! How about you ! Sir Have you ate you lunch ? ")
            query = takeCommand().lower()         
        elif(hour > 16) and (hour < 20 ):
            speak("I am fine Sir ! Thanks for your concern ! How about you ! Sir Have you ate you snacks ? ")
            query = takeCommand().lower()       
        else:
            speak("I am fine Sir ! Thanks for your concern ! How about you ! Sir Have you ate you dinner ? ") 
            query = takeCommand().lower()
        if("yes" in query):
            speak("Okay cool let's get back to the work")
        elif('after' in query) or ('later' in query):
            speak("okay sir but please don't forget to eat ! Eat compelte after your work get complete ! ")
        elif('no' in query) or ('have not' in query):
            speak("Sir go and eat your meal before your mom yell at you")                           
    elif(msg == 1):
        speak("Hello Sir i am doing good ! What about you ?")
    elif(msg == 2):
        speak("hey sir i am good ! what about you ?")
    else:
        speak("i am very well sir ! how you doing ?")    

#MainFunction
def main():
    def clear(): return os.system("cls")
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    #spotify_path = 'C:/Users/home/AppData/Roaming/Spotify/Spotify.exe %s'

    clear()
    time()
    greetMe()
    #username()

    while True:
        query = takeCommand().lower()

        if ("close" in query) or ("exit" in query) :
            hour = dt.datetime.now().hour
            if hour > 19 or hour < 7:
                speak("Signing off ! Closeing friday program sir ! It's time to sleep good night")
            else:
                speak("Signing off ! Closing friday program ! Have a good day sir")    
            exit()

        elif "open browser" in query:
            speak("Opening google chrome sir !")
            wb.get(chrome_path).open_new_tab("https://google.com")

        elif "google" in query and "search" in query :
            speak("Sir What you want to search on google ?")
            query= takeCommand().lower()
            speak("Searching for results on Google ! ")
            wb.get(chrome_path).open_new_tab(f"https://www.google.com/search?q={query}")

        elif "youtube" in query and "search" in query :
            speak("Sir What you want to search on Youtube ?")
            query = takeCommand().lower()
            speak("Searching for results on Youtube sir ! ")
            wb.get(chrome_path).open_new_tab(f"https://www.youtube.com/results?search_query={query}")
            td.sleep(3)

        elif ("open youtube" in query):
            speak("Opening youtube sir !")
            wb.get(chrome_path).open_new_tab("youtube.com")

        elif "all window" in query:
            pg.hotkey('win','d')      

        elif "the time" in query:
                hour = dt.datetime.now().hour
                strTime = dt.datetime.now().strftime("%H:%M:%S") 
                if hour > 0 and hour < 12:
                    speak(f"Sir it's {strTime} A M")
                else:
                    speak(f"Sir it's {strTime} P M")   

        elif "who are you" in query:
            speak("Hello There ! I am friday 1 point o ! Female Replacement Intelligent Digital Assistant Youth ! An artificial intelligent Assistant coded by Krishna inspired by Tony Stark")
            speak("I am developed for an python Artificial Intelligent project and making your life easy ! I can do many things like search any query on Google , search videos on Youtube , Play music , Opening any app on your PC and many more !")
            speak("What should i do for you Sir ?")

        elif 'how are you' in query:
            talk()
            

        elif ("WhatsApp" in query) or ("whatsapp" in query):
            speak("Opening Whatsapp sir !")
            wb.get(chrome_path).open_new_tab("web.whatsapp.com")   

        elif "app" in query:
            speak("What is the app name : ")
            appname = takeCommand().lower()
            if "valent" in appname or "vellore" in appname:
                appname = "valorant"
            run(appname) 

        elif "volume up" in query or "increase volume" in query:
            pg.press("volumeup")  

        elif "volume down" in query or "decrease volume" in query:
            pg.press("volumedown")

        elif "volume mute" in query or "mute" in query :
            pg.press("volumemute")  

        elif "change window" in query:
            pg.hotkey('alt', 'tab') 

        elif "first" in query and "video" in query:
            pg.click(x=380, y=300, duration=0.5, button='left')         

                       

        elif "favourite music" in query and "youtube" in query :
            fav_playlist()           

        else:
            print("somthing went worng ! please try again")    

         

main()

    
        
