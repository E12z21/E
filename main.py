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
        data = r.listen(source, timeout=30, phrase_time_limit=20)
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
    elif 'locate' in command:
        playsound('audio\\locating.mp3')
        c.handleMapsCommands(command)
    elif 'go to' in command:
        c.handleURLCommands(command)
    elif 'set volume to' in command or command == 'mute':
        c.handleAudioCommands(command)
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
                try:
                    command = command.replace(' in google maps', '" in google maps')
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
    elif 'with a due date of' in command or 'check when' in command or 'from events' in command or command == 'clear all events' or command == 'get events':
        if 'add' in command:
            command = str(command).lower().replace('add ', 'add "').replace(' to events with a due date of ', '" to events with a due date of "')
        elif 'check when' in command:
            command = str(command).lower().replace('check when ', 'check when "').replace(' is due', '" is due')
        elif 'remove' in command:
            command = str(command).lower().replace('remove ', 'remove "').replace(' from events', '" from events')
        else:
            print('')
        print(command)
        print('Processing scheduler request')
        c.handleTimetablerCommands(command)
    elif ' + ' in str(command).lower() or ' minus ' in str(command).lower() or ' x ' in str(command).lower() or ' / ' in str(command).lower() or ' ^ ' in str(command).lower():
        playsound('audio\\math.mp3')
        answer = c.handleMathCommand(command)
        print(answer)
    elif 'what is the weather' in command:
        playsound('audio\\weather.mp3')
        c.handleManualWeatherCommands(command)
    elif str(command).lower() == 'hey jarvis':
        playsound('audio\\wake.mp3')
    elif str(command).lower() == 'what is the time':
        print('Getting time')
        print(str(c.handleAutoTimeCommands()))
    elif 'what is the time in ' in str(command).lower():
        print('Getting time')
        c.handleManualTimeCommands(command)
    else:
        playsound('audio\\error.mp3')