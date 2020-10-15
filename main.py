from Commands import app_opener, web_searches, command_handler
from playsound import playsound

a = app_opener.AppOpener()
w = web_searches.Web()
c = command_handler.Handler()

playsound('audio\\music.mp3')
playsound('audio\\welcome.mp3')
while True:
    command = input('>>>')
    command = str(command).lower()
    if 'open' in command:
        playsound('audio\\opening_app.mp3')
        c.handleOpenCommands(command)
    elif 'go to' in command:
        c.handleURLCommands(command)
    elif 'search' in command:
        c.handleSearchCommands(command)
    elif str(command).lower() == 'exit':
        playsound('audio\\goodbye.mp3')
        break
    else:
        playsound('audio/error.mp3')
