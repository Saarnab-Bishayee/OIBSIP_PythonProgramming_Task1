import pyttsx3
import speech_recognition as sr
import wikipedia as wkp
import webbrowser as wb
from datetime import datetime
import time
import smtplib
from email.message import EmailMessage

engine = pyttsx3.init('sapi5')
engine.setProperty('rate',180)
engine.setProperty('volume',1)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def pns(text):
    print(text)
    speak(text)

def WishMe():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        pns("Good Morning Sir")
    elif 12 <= hour < 18:
        pns("Good Afternoon Sir")
    else:
        pns("Good Evening Sir")
    pns("I'm your Personal Voice Assistant. Nice to meet you!")
    pns("How should I help you, Sir?")

r=sr.Recognizer()
def listen():
    print("Initializing Voice Assistant Microphone:\nPlease wait...")
    with sr.Microphone() as source:
        print("Now speak...")
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=4)
            text = r.recognize_google(audio)
            print(f"Heard: {text}")
            return text
        except sr.UnknownValueError:
            pns("Sorry, I couldn't understand that.")
        except sr.WaitTimeoutError:
            pns("You didn't speak in time.")
        return 'None'

def WikiSearch():
    pns("Enter search query: ")
    try:
        query = listen()
        pns(f"Searching for {query}")
        pns(wkp.summary(query, sentences=2))
    except ExceptionGroup:
        pns("Sorry couldn't hear that, Please try again.")
        return WikiSearch()

def Website():
    url=''
    pns("Which website would you like me to open?")
    try:
        web = listen().lower()
        if "youtube" in web:
            url = "youtube.com"
        elif "google" in web:
            url = "google.com"
        elif "linkedin" in web:
            url = "linkedin.com"
        pns(f"Opening {web}...")
        wb.open(url)
    except ExceptionGroup:
        pns("Sorry couldn't hear that, Please try again.")
        return Website()

def actual_time():
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    if 12 < hour < 24:
        hour-=12
        pns(f"The time is {hour}:{minute}:{second}pm")
    elif hour == 12:
        pns(f"The time is {hour}:{minute}:{second}pm")
    elif hour == 0:
        pns(f"The time is {hour+12}:{minute}:{second}am")
    else:
        pns(f"The time is {hour}:{minute}:{second}am")

def actual_date():
    now = datetime.now()
    mname = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
             7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    pns(f"The date is {now.day}th of {mname[now.month]} of year {now.year}")

def sendMail():
    try:
        mail = EmailMessage()
        pns("Please say the message you want to send.")
        text=listen()
        mail.set_content(text)
        pns("Please enter the Subject of the email.")
        subject = input()
        mail['Subject'] = subject
        mail['From'] = "<Your Email-id>"
        pns("Please enter the receiver's email address.")
        recipient=input()
        mail['To'] = recipient
        pns("Sending mail...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('<Your Email-id>', '<Your App Password>')
            smtp.send_message(mail)
        pns("Email sent successfully!")
    except smtplib.SMTPException:
        pns("Sorry, Email could not be sent.\nPlease try again.")
        return sendMail()

def Menu():
    pns("""These are some functions which I can perform:
            Respond to Hello,
            Tell you the Time,
            Tell you the Date,
            Google Search for you,
            Open Selected Websites for you,
            Send a Mail for you,
            To exit, say Goodbye or No Thanks,
            Thank you for your time""")

def main():
    WishMe()
    while True:
        msg = listen().lower()
        if "hello" in msg:
            pns("Hello Sir, I'm your Personal Voice Assistant!\nHow would you like me to help you?")
        elif "what can you do" in msg:
            Menu()
        elif "what is the time" in msg:
            actual_time()
        elif "what is the date" in msg:
            actual_date()
        elif "wikipedia search" in msg:
            WikiSearch()
        elif "open website" in msg:
            Website()
        elif "send mail" in msg:
            sendMail()
        elif "good bye" in msg or "no thanks" in msg:
            pns("Goodbye Sir, Have a nice day!")
            break
        else:
            pns("Please try again.")
        time.sleep(0.5)
        pns("Any other queries, Sir?")

if __name__ == "__main__":
    main()