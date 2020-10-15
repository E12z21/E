# J.A.R.V.I.S - Personal Assistant
## Overview

J.A.R.V.I.S is a personal assistant that can - 

- automate tasks on your computer
- Give daily reports of your computer usage, internet usage, etc.
- schedule tasks to be completed at other times
- Uses AI-generated speech to talk
- Listens to your voice using Google Speech API

## Log

v0.2 - Currently, speech recognition is not working (because pyaudio and speech recognition decide not to work on my computer!). Have to type in commands into Python Console. Can automate searches on the internet, open apps. Can also talk using AI generated speech. v0.2 only compatible with Windows devices. Upcoming features would be to be able to close apps, create reports, a scheduler, an inbuilt timetable, more apps that can be opened (and closed) via JARVIS, bug fixes, etc. Location searches, being able to tell the time, get weather from weather api, etc.

## In Depth

JARVIS is currently (v0.2) split into 4 components, the `app_opener`, which handles app opening, `web_searches`, which manages web searches, the `command_handler`, which relays command inputed by the user to functions inside the `app_opener` and `web_searches` module and finally the `main.py` (for v0.2 it's called `test.py`), which combines the three modules together and actually runs JARVIS.

```Python

print('Thanks for Reading!')

```

