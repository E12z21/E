from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

class Audio(object):
    def __init__(self):
        self.command = None
        self.volume = None
        self.sessions = AudioUtilities.GetAllSessions()

    def changeVolume(self, value):
        if int(value) <= 100:
            self.value = int(value)/100
            for session in self.sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                # print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
                volume.SetMasterVolume(self.value, None)
                print('Volume Changed')
        else:
            print('Sorry but the volume number you typed is incorrect')

