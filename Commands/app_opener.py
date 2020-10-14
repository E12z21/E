import os


class AppOpener(object):
    def __init__(self):
        self.command = None
        self.exe = {
            'word': 'C:\\"Program Files (x86)"\\"Microsoft Office"\\root\Office16\WINWORD.EXE',
            'powerpoint': 'C:\\"Program Files (x86)"\\"Microsoft Office"\\root\Office16\POWERPNT.EXE',
            'teams': 'C:\\Users\\testing\AppData\Local\Microsoft\Teams\\Update.exe --processStart "Teams.exe"',
            'zoom': 'C:\\Users\\testing\AppData\Roaming\Zoom\\bin\Zoom.exe',
            'firefox': 'C:\\"Program Files"\\"Mozilla Firefox"\\firefox.exe',
            'chrome': 'C:\\"Program Files (x86)"\Google\Chrome\Application\chrome.exe --allow-outdated-plugins',
            'pycharm': '"C:\\"Program Files"\\JetBrains\\"PyCharm Community Edition 2018.2"\\bin\pycharm64.exe"',
            'terminal': '%windir%\system32\cmd.exe',
            'notepad ++': 'C:\\"Program Files"\\"Notepad++"\\"notepad++.exe"',
            'notepad': '%windir%\system32\\notepad.exe',
            'filmora': 'C:\\"Program Files (x86)"\Wondershare\\"Wondershare Filmora (CPC)"\\"Wondershare Filmora9.exe"',
        }
        self.keys = [
            'word',
            'powerpoint',
            'teams',
            'zoom',
            'firefox',
            'google',
            'pycharm',
            'terminal',
            'notepad ++',
            'notepad',
            'filmora'
        ]

    def open(self, path):
        self.command = 'start {}'.format(path)
        os.system('cmd /c "{}"'.format(self.command))
        return
