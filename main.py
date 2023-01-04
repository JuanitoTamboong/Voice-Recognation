import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
#female voice
#voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)
def talk(text):
     engine.say(text)
     engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'code' in command:
             command = command.replace('code', '')
            print(command)
    except:
        pass
    return command

def run_code():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who created you' in command:
        talk('My master  Juanito Tamboong is created me ')
    elif 'who are you' in command:
        talk('I am code')
        talk('created in year 2023')
    elif 'juanito tamboong' in command:
        talk('Juanito tamboong 23 years old,2nd year student,studied at romblon state university')
        talk('taking bachelor of science and infomation technology')
        talk('from Budiong Odiongan Romblon')
    elif 'my girlfriend name' in command:
        talk('Your Girlfriend is Margelyn Vicente')
    elif 'i love you' in command:
        talk(' i love you too sir as my creator')
    elif 'good morning' in command:
        talk('good morning sir' + 'have a pleasant morning')
    elif 'good afternoon' in command:
        talk('good afternoon sir' + 'have a nice afternoon')
    elif 'good evening' in command:
        talk('good evening sir' + 'have a great evening')
    elif 'thank you' in command:
        talk('Your welcome sir!!!')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry sir say the command again')

while True:
    run_code()
