from datetime import datetime
import os

class Time(object):
    def __init__(self):
        pass

    def returnTimeAuto(self):
        present = datetime.now()
        return str(present.strftime('%a %d %b %Y %H:%M:%S'))

    def returnManualTime(self, city):
        os.system('cmd /c C:\\"Program Files (x86)"\Google\Chrome\Application\chrome.exe --allow-outdated-plugins https://www.google.com/search?q=time+in+{}'.format(city))