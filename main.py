from Commands import app_opener, web_searches, command_handler
from playsound import playsound
import speech_recognition as sr

a = app_opener.AppOpener()
w = web_searches.Web()
c = command_handler.Handler()
r = sr.Recognizer()

playsound('audio\\music.mp3')
playsound('audio\\welcome.mp3')
while True:
    command = ''
    with sr.Microphone() as source:
        data = r.listen(source, timeout=20, phrase_time_limit=10)
    try:
        command = str(r.recognize_google(data)).lower()
        print('>>> {}'.format(command))
    except:
        print('Nothing')
    if 'open' in command:

        c.handleOpenCommands(command)
    elif 'go to' in command:
        c.handleURLCommands(command)
    elif 'search' in command:
        c.handleSearchCommands(command)
    elif 'how are you' in command:
        playsound('audio\\hru.mp3')
    elif str(command).lower() == 'exit':
        playsound('audio\\goodbye.mp3')
        break
    elif str(command).lower() == 'ok':
        playsound('audio\\revert.mp3')
    else:
        playsound('audio\\error.mp3')