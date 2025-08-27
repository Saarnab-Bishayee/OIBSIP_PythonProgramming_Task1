# 🗣️ Smart Voice Assistant

## 🎯 Objective
The objective of this project is to build a **voice-controlled personal assistant** using Python. The assistant can respond to greetings, tell the date and time, perform web searches, open websites, send emails, and interact with the user through speech.

---

## 🛠 Steps Performed
1. Initialized the text-to-speech engine (`pyttsx3`) for spoken responses.  
2. Used `speech_recognition` to capture and process user voice input.  
3. Integrated multiple functionalities:
   - Respond to greetings (Hello)
   - Tell the current **time** and **date**
   - Perform **Wikipedia search**
   - Open selected websites (Google, YouTube, LinkedIn)
   - Send emails using **SMTP**
   - Exit gracefully on commands like "Goodbye" or "No Thanks"
4. Designed a continuous loop to keep listening and responding until the user exits.  
5. Implemented error handling for unrecognized or delayed voice inputs.  

---

## ⚙️ Tools & Libraries Used
- **Python 3.13**  
- `pyttsx3` → For text-to-speech conversion.  
- `speech_recognition` → For voice input and recognition.  
- `wikipedia` → To fetch quick summaries.  
- `webbrowser` → To open websites in the browser.  
- `datetime` → To get current time and date.  
- `time` → To manage delays in responses.  
- `smtplib` & `email.message` → To send emails using SMTP.  

---

## ✅ Outcome
- A fully functional **Smart Voice Assistant** capable of:  
  - Responding to greetings 👋  
  - Telling time ⏰ and date 📅  
  - Searching Wikipedia 📚  
  - Opening websites 🌐  
  - Sending emails ✉️  
  - Exiting on user’s command 🚪  
- Provided a **hands-on experience** in integrating multiple Python modules into a single interactive application.  
- Improved understanding of **voice interfaces** and real-world automation with Python.  

---

✨ This project is part of my **Python Programming Internship at Oasis Infobyte** (Task 1).
