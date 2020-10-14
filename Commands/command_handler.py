from Commands import web_searches, app_opener
from playsound import playsound

class Handler(object):
    def __init__(self):
        self.a = app_opener.AppOpener()
        self.w = web_searches.Web()
        self.command = None

    def handleOpenCommands(self, query):
        query = str(query).replace('open ', '').strip()
        keyFound = False
        keys = self.a.keys
        exe = self.a.exe
        for key in keys:
            if str(key) in query:
                command = exe[str(key)]
                keyFound = True
                self.a.open(path=command)
                break

        if keyFound is False:
            try:
                self.a.open(path=query)
            except:
                print('Sorry, the command you typed does not exist')

    def handleURLCommands(self, query):
        query = str(query).split(' ')
        url = str(query[2]).strip()
        browser = str(query[4]).strip()
        keys = self.w.keys
        exe = self.a.exe
        for key in keys:
            if str(key).lower() == str(browser).lower():
                if str(key).lower() == 'chrome':
                    playsound('audio/search_chrome.mp3')
                else:
                    playsound('audio/search_firefox.mp3')
                command = str(exe[str(key)]) + ' ' + str(url)
                self.w.goToUrL(command)

    def handleSearchCommands(self, query):
        query = str(query).split('"')
        search = str(query[1]).replace(' ', '+')
        browser = str(query[2]).replace(' in ', '').strip()
        keys = self.w.keys
        exe = self.a.exe
        for key in keys:
            if str(key).lower() == str(browser).lower():
                if str(key).lower() == 'chrome':
                    playsound('audio/search_chrome.mp3')
                else:
                    playsound('audio/search_firefox.mp3')
                command = str(exe[str(key)]) + ' https://www.google.com/search?q={}'.format(search)
                self.w.goToUrL(command)