import tkinter as Tk
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wolframalpha
import random
from requests import get
import wikipedia
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
import webbrowser
import pywhatkit as kit
import sys
import pyautogui
import keyboard
import pyjokes
from playsound import playsound
from PyDictionary import PyDictionary as Diction
import speedtest
from pywikihow import search_wikihow
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=(5))
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("good evening")
    speak("I am jarvis sir . How can i help u...?")

def screenshot():
    speak("ok sir ..! what should i name the file")
    path = takecommand()
    path1name = path + ".png"
    path1 = "E:\\jarvis\\jarvis boy\\jarvis screenshot\\"+ path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("E:\\jarvis\\jarvis boy\\jarvis screenshot")
    speak("Here is your screenshot")

def OpenApp():

    speak("ok..! Sir wait a second")

    if 'code' in query:
        os.startfile("E:\Microsoft VS Code\Microsoft VS Code\Code.exe")   

    elif 'chrome' in  query:
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    elif 'telegram' in query:
        os.startfile("E:\rishi\Telegram Desktop\Telegram.exe")

    elif 'ldplayer' in query:
        os.startfile("D:\LDPlayer\LDPlayer3.0\dnplayer.exe")

    elif 'cmd' in query:
        os.system("start cmd")

    elif 'android studio' in query:
        os.startfile("C:\Program Files\Android\Android Studio\bin\studio64.exe")

    elif 'maps' in query:
        webbrowser.open('https://www.google.com/maps/@21.1089422,79.075803,15z')

        speak("Your order is completed Sir ......!")

def Dict():
    speak("Activited Dictionary sir ..!")
    speak("what you want to know sir ..!")
    probl = takecommand()

    if 'meaning' in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of","")
        probl = probl.replace("meaning of","")
        result = Diction.meaning(probl)
        speak(f"The Meaning For {probl} is {result}")


    elif 'synonym' in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of","")
        probl = probl.replace("synonym of","")
        result = Diction.synonym(probl)
        speak(f"The synonym For {probl} is {result}")

    elif 'antonym' in probl:
        probl = probl.replace("what is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of","")
        probl = probl.replace("antonym of","")
        result = Diction.antonym(probl)
        speak(f"The antonym For {probl} is {result}")

    speak("Exited Dictionary Sir ..!")










app = wolframalpha.Client("A57T4Y-KEYR9KW5Y8")
        
        

def CloseApp():
    speak("Wait a Second . Sir ....!")

    if 'chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'code' in query:
        os.system("TASKKILL /F /im code.exe")
        
    elif 'telegram' in query:
        os.system("TASKKILL /F /im Telegram.exe")

    elif 'android studio' in query:
        os.system("TASKKILL /F /im studio64.exe")

    elif 'ldplayer' in query:
        os.system("TASKKILL /F /im dnplayer.exe")

    elif 'maps' in query:
        os.system("TASKKILL /F /im chrome.exe")
        
    elif 'instagram' in query:
        os.system("TASKKILL /F /im chrome.exe")
    
    elif 'youtube' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'stackoverflow' in query:
        os.system("TASKKILL /F /im chrome.exe")

def YoutubeAuto():
    speak("What you want me to do Sir ...!")
    comm = takecommand()
    if 'pause ' in comm:
        keyboard.press('k')

    elif 'restart' in comm:
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press('m')

    elif 'unmute' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'backspace' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    elif 'exit full screen' in comm:
        keyboard.press('f')
        
    elif 'turn on captions' in comm:
        keyboard.press('c')

    speak("done sir!")
def ChromeAuto():
    speak("chrome automation Activeted Sir ...!")

    command = takecommand()

    if 'close tab' in command:
        keyboard.press_and_release('ctrl + w')

    elif 'change tab' in command:
        keyboard.press_and_release('ctrl + tab')

    elif 'go to home ' in command:
        keyboard.press_and_release('alt + home')

    elif 'open new tab' in command:
        keyboard.press_and_release('ctrl + n')

    elif 'opne new incognito tab' in command:
        keyboard.press_and_release('ctrl + shift + n')

    elif 'last tab' in command:
        keyboard.press_and_release('ctrl + shift + tab')

    elif 'history' in command:
        keyboard.press_and_release('ctrl + history')

    elif 'download' in command:
        keyboard.press_and_release('ctrl + j')

    elif 'add bookmark' in command:
        keyboard.press_and_release('ctrl + d')

    elif 'print' in command:
        keyboard.press_and_release('ctrl + p')

def SpeedTest():
    speak("Checking the speed sir .!")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)


    if 'uploading' in query:
        speak(f"The uploading Speed Is {correctUpload}mbp s")

    elif 'downloading' in query:
        speak(f"The downloading Speed Is {correctDown}mbp s")

    else:
        speak(f"the uploading Speed Is {correctUpload} and the downloading Speed Is {correctDown}mbp s") 







    
    
    
    app = wolframalpha.Client("A57T4Y-KEYR9KW5Y8")
       
       
        
if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        if 'hello' in query:
            speak("Hello Sir how can I help u...?")

        elif 'how are you' in query:
            speak("I Am Fine Sir . How are you")

        elif 'you need a break' in query:
            speak("OK Sir call me .if u need anything...!")
            speak("if u need me say jarvis i will be back ...!")
            break
         
        
        
            
        elif "open command prompt" in query:
            os.system("start cmd")

        elif 'youtube search' in query:
            speak("ok sir! This Is What I Found On Youtube..")
            query = query.replace("Jarvis","")
            query = query.replace("youtube search","")           
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir!")

        elif 'google search' in query:
            speak("ok sir! This Is What I Found On Google..!")
            query = query.replace("Jarvis","")
            query = query.replace("google search","")           
            web = 'https://www.google.com/search?q=' + query
            webbrowser.open(web)
            speak("Done sir!")

        elif 'launch' in query:
            speak("Launching sir......!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak ("done sir")
            



        elif "open camera" in query:
          cap = cv2.VideoCapture(0)
          while True:
                ret, img = cap.read()
                cv2.imshow('webcam, img')
                k = cv2.waitkey(50)
                if k==27:
                    break;
                    cap.release()
                    cv2.destroyAllWindows()
        elif 'temperature' in query:
            res = app.query(query)
            speak(next(res.results).text)
        elif 'calculate' in query:
            speak("what should i calculate?")
            gh = takecommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)
            
        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")
            
        elif "wikipedia" in query:
            speak("searching from wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipeida")
            speak(results)
            #print(results)
            
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            
            
        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com")
        
        
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")
        
        
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        
        
        elif "open amazon" in query:
            webbrowser.open("https://www.amazon.in")
        
        
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com")    

        elif 'screenshot' in query:
            screenshot()

        elif 'code' in query:
            OpenApp()

        elif 'chrome' in  query:
            OpenApp()

        elif 'telegram' in query:
            OpenApp()

        elif 'ldplayer' in query:
            OpenApp()

        elif 'cmd' in query:
            OpenApp()

        elif 'android studio' in query:
            OpenApp()

        elif 'maps' in query:
            OpenApp()
            
        elif 'close chrome' in query:
            CloseApp()
        
        elif 'close telegram' in query:
            CloseApp()

        elif 'close code' in query:
            CloseApp()

        elif 'ldplayer' in query:
            CloseApp()

        elif 'close android studio' in query:
            CloseApp()

        elif 'maps' in query:
            CloseApp()

        elif 'close instagram' in query:
            CloseApp()
        
        elif 'close stackoverflow' in query:
            CloseApp()

        elif 'pause ' in query:
            keyboard.press('k')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'unmute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'backspace' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'exit full screen' in query :
            keyboard.press('f')
        
        elif 'turn on captions' in query:
            keyboard.press('c')

        elif 'youtube automation' in query:
            YoutubeAuto()

        elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'change tab' in query:
            keyboard.press_and_release('ctrl + tab')

        elif 'go to home ' in query:
            keyboard.press_and_release('alt + home')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'opne new incognito tab' in query:
            keyboard.press_and_release('ctrl + shift + n')

        elif 'last tab' in query:
            keyboard.press_and_release('ctrl + shift + tab')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + history')

        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'add bookmark' in query:
            keyboard.press_and_release('ctrl + d')

        elif 'print' in query:
            keyboard.press_and_release('ctrl + p')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'repeat my word' in query:
            speak("OK Sir! I will Repeat What You Say ..!")
            jj = takecommand()
            speak(f"You said : {jj}")

        elif 'my location' in query:
            speak("ok sir")
            webbrowser.open('https://www.google.com/maps/place/65C,+New+Sneh+Nagar,+Nagpur,+Maharashtra+440015/@21.1082654,79.0684765,95m/data=!3m1!1e3!4m5!3m4!1s0x3bd4bf79df9a4c4d:0xab5cd367bc4ac92d!8m2!3d21.108536!4d79.0686')

        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            speak("Enter the time sir!")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time TO Wake Up Sir ...!")
                    playsound('avengers.mp3')
                    speak("Alarm closed")

                elif now>time:
                    break

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.tile("Youtube Video Downloader")

            Label(root,text = "Youtube Video Downloader",font ='arial 15 bold').pack()
            link = StringVar()
            Label(root,text ='Paste Yt video URL Here',font='arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable= link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.stream.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x = 180,y=210)
                
            Button(root,text = "Download",font = 'arial 15 bold',bg= 'pale violet red',padx= 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            speak("Video Downloaded")


        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            speak("You Told Me To Remind You that :"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            speak("You Tell Me That"+remember.read())


        elif 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'internet speed' in query:
            SpeedTest()

        elif 'how to' in query:
            speak("Getting Data from the Internet !")
            op = query.replace("jarvis", "")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)





        elif 'send message' in query:
            kit.sendwhatmsg("+919834776494", "this is testing protocol",2,45)
        
        
        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif 'jokes' in query:
            get = pyjokes.get_joke()
            speak(get)

        
        elif "no thanks" in query:
            speak("thanks for using sir... Have a good day")
        sys.exit()
        
        speak("sir,do you have any other work")
