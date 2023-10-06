import pyttsx3#pip install pyttsx3
import speech_recognition as sr#pip install SpeechRecognition
import datetime
print(                                          '\t','\t','\t','\t','VIRTUAL QUIZ'                                          )
a=pyttsx3.init('sapi5')
voices=a.getProperty('voices')
a.setProperty('voices',voices[len(voices)-1].id)
def speak(audio):
  audio=str(audio)

  print('computer:'+audio)
  
  a.say(audio)
  a.runAndWait() 
def greet():

  
  h=int(datetime.datetime.now().hour)
  if h>=0 and h<12:
      speak("good morning")
  if h>=12 and h<12:
         speak("good afternoon")
  if h>=18 and h!=0:
       speak("good evening")

greet()           


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =0.6
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        

    except sr.UnknownValueError:
        
        query = input(" ")
    return query
speak("tell me your name")
d=myCommand()

dict={"where is qutumb minar":'delhi',"where is taj mahal":"agra","father of nation":"mahatma gandhi","Who was the first woman Prime Minister of India":'indira gandhi'}#you can add more questions here
speak('hi'),speak(d),speak('this is your virtual  quiz. Are you ready for the quiz')
query=myCommand()
c=0
if query=="yup"or query=="Yes" or query=="yes":
   
    question=dict.keys()
    answer=dict.values()
    for i in question:
    
      speak(i)
      query=myCommand()
      query=query.lower()
      for j in answer:
        if j==query:
            
            c=c+1
if c!=0:
    speak("your score is"),speak(c)

