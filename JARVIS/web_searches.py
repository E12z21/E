import os


class Web(object):
    def __init__(self):
        self.command = None
        self.search = None
        self.keys = ['chrome', 'firefox', 'google maps']

    def goToUrL(self, command):
        self.command = command
        os.system('cmd /c "{}"'.format(self.command))

    def pingGoogle(self):
        self.command = 'ping google.com'
        os.system('cmd /c "{}"'.format(self.command))
