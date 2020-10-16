from JARVIS import command_handler
from playsound import playsound
import speech_recognition as sr

c = command_handler.Handler()
r = sr.Recognizer()

playsound('audio\\music.mp3')
playsound('audio\\welcome.mp3')
while True:
    command = ''
    with sr.Microphone() as source:
        data = r.listen(source, timeout=30, phrase_time_limit=10)
    try:
        command = str(r.recognize_google(data)).lower()
        print('>>> {}'.format(command))
    except:
        print('Nothing')
    if 'open' in command:
        c.handleOpenCommands(command)
    elif 'close' in command:
        playsound('audio\\closing_app.mp3')
        c.handleCloseCommands(command)
    elif 'go to' in command:
        c.handleURLCommands(command)
    elif 'search' in command:
        command = command.replace('search ', 'search "')
        try:
            command = command.replace(' in chrome', '" in chrome')
            c.handleSearchCommands(command)
        except:
            try:
                command = command.replace(' in firefox', '" in firefox')
                c.handleSearchCommands(command)
            except:
                playsound('audio\\error.mp3')
        print(command)
    elif 'how are you' in command:
        playsound('audio\\hru.mp3')
    elif 'what is your name' in command:
        playsound('audio\\welcome.mp3')
    elif str(command).lower() == 'exit':
        playsound('audio\\goodbye.mp3')
        break
    elif str(command).lower() == 'ok':
        playsound('audio\\revert.mp3')
    elif str(command).lower() == '':
        continue
    elif ' + ' in str(command).lower() or ' minus ' in str(command).lower() or ' x ' in str(command).lower() or ' / ' in str(command).lower() or ' ^ ' in str(command).lower():
        playsound('audio\\math.mp3')
        answer = c.handleMathCommand(command)
        print(answer)
    else:
        playsound('audio\\error.mp3')