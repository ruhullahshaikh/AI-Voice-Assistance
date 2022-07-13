import  pyttsx3 #text to speech
import speech_recognition as sr #specch recognition
import datetime #for datetime
import wikipedia #for wikipedia
import webbrowser #foe opening websites
import os #operating system
import smtplib #sending email
import sys 

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif  hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak('Good Evevning')

    speak('I am Your Voice Assistant, please tell me how may I help You!')

def takeCommand(): #it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:  # use the default microphone as the audio source
        print("Listening....")
        r.pause_threshold=0.5
        audio=r.listen(source)  # listen for the first phrase and extract it into audio data

    try:
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)

        print("I can't Listen Please Say That Again.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ruhullahshaikh@eng.rizvi.edu.in', '70586275')
    server.sendmail('shaikhruhullahsaifullah@gmail.com',to, content)
    server.close()

if __name__=='__main__':
    #speak('Ruhullah')
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower() #Logic for executing task
        if  'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=5)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
       
        elif 'date' in query:
            strDate=datetime.date.today()
            print(strDate.day,strDate.month,strDate.year)
            speak("today date is {strDate}")
            print(strDate)

        elif 'chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        #elif 'play music' in query:
          #  music_dir = "C:\\Users\\shaik\\Music"
         #   songs = os.listdir(music_dir)
            #print(songs)    
           # os.startfile(os.path.join(music_dir, songs[0]))

        elif 'email' in query:
            try:
                print('What conversation you want to say Please tell me?')
                speak('What conversation you want to say Please tell me?')
                content = takeCommand()
                to="shaikhruhullahsaifullah@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        
        elif "quit" in query:
            sys.exit(0)
        elif "exit" in query:
            sys.exit(0)

        elif 'your name' in query:
            speak('Voice Assistant')
            print("Voice Assistant")

        elif 'how are you' in query:
            speak("I am fine. What about yourself?")
            print("I am fine. What about yourself?")

        elif 'college name' in query:
            speak('Rizvi College of Enginnering')
            print('Rizvi College of Enginnering')
            
        elif 'principal' in query:
            
            print("Dr. Varsha Shah")
            speak("Dr. Varsha Shah")
            
        elif 'head of department' in query:
            print("Dr. Sampath")
            speak("Dr. Sampath")
            
        elif 'teacher' in query:
            print("Mr. Ashfaque, Mr. Vikas, Mr. Amit Redkar, Mr. Dinesh, Mrs. Rukhsar, Mrs. Ronica Raj")
            speak("Mr. Ashfaque, Mr. Vikas, Mr. Amit Redkar, Mr. Dinesh, Mrs. Rukhsar, Mrs. Ronica Raj")

        elif 'principal office' in query:
            print("first floor Room No. 101")
            speak("first floor Room No. 101")

        elif 'computer lab' in query:
            print("Second Floor Room No.205")
            speak("Second Floor Room No.205")

        elif 'computer engineering class' in query:
            print("At Second Floor")
            speak("At Second Floor")

        elif 'college office' in query:
            print("At first floor after principal office")
            speak("At first floor after principal office")

        elif 'location' in query:
            print("carter road bandra west")
            speak("carter road bandra west")

        elif '2nd year' in query:
            print("Room No. 202")
            speak('Room No. 202')
        elif '1st year' in query:
            print("Room No. 201")
            speak('Room No. 201')
        elif '3rd year' in query:
            print("Room No. 203")
            speak('Room No. 203')
        elif '4th year' in query:
            print("Room No. 204")
            speak('Room No. 204')
        elif 'second year' in query:
            print("Room No. 202")
            speak('Room No. 202')
        elif 'first year' in query:
            print("Room No. 201")
            speak('Room No. 201')
        elif 'third year' in query:
            print("Room No. 203")
            speak('Room No. 203')
        elif 'fourth year' in query:
            print("Room No. 204")
            speak('Room No. 204')
        elif 'company visited' in query:
            print("IBM, TATA, VISTEX,HP,STALLION,MIDCO,IGATE,SAP,ETA,L&T INSFOSYS For more information please visit 'https://eng.rizvi.edu.in/placements/companies-visited/'")
            print("For more Information please Visit 'https://eng.rizvi.edu.in/placements/'")
            speak('IBM, TATA, VISTEX,HP,STALLION,MIDCO,IGATE,SAP,ETA,L&T INSFOSYS etc')

        elif 'contact' in query:
            print("https://eng.rizvi.edu.in/ or http://rcoe.co.in/")
            speak('please visit following links')

        elif 'placement record' in query:
            print("In 2017-18, 112\n2018-19, 110\n2019-20,64 and in\n2020-21,82 students got palcement. Gor more information please visit 'https://eng.rizvi.edu.in/placements/placement-record/'")
            print("For more Information please Visit 'https://eng.rizvi.edu.in/placements/'")
            speak('In 2017 & 18 112 2018 19 110 2019 20 64 and 2020 21 82 students got palcement')

        elif 'website' in query:
            webbrowser.open("https://eng.rizvi.edu.in/")

        elif('collection') in query:
            print("Books » 28170\nJournals » 50\nOnline Databases » 04\nCD Collection » 450\nNewspapers » 14\ne-books » 384") 
            print("For more Information please Visit 'https://eng.rizvi.edu.in/library/'")
            speak('Books 28170 Journals 50 online database 4 and many more')
        elif('services') in query:
            print("News Paper Clipping Service\nCurrent Awareness Service\nReference Service\nReferral Service\nIndexing Service through OPAC\nNew Arrivals Display\nAccess to Back issues of Journals\nBook Bank service\nScholar Card for Toppers")
            print("For more Information please Visit 'https://eng.rizvi.edu.in/library/libraryservices'")
            speak('print("News Paper Clipping Service Current Awareness Service Reference Service Referral Service Indexing Service through OPAC etc')
        elif('rules') in query:
            print("Books are issued for 7 days only.\nThose who fails to return the books within 30 days , there Library membership will be discontinued for the current semester.\nReference books taken out of Library without permission will be charged a fine of Rs.25/- per day\nOver night issue books should be return before 10.30 a.m. late will be charged a fine of Rs. 50/- per day including Saturday and Holidays.\nFine will be charged for holidays if books not returned on the next working day")
            print("For more Information please Visit 'https://eng.rizvi.edu.in/libary/'")
            speak("Read the beolw rules and regulations")
