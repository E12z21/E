![J.A.R.V.I.S - Personal Assistant](https://github.com/J-A-R-V-I-S-ai/J.A.R.V.I.S/blob/main/JARVIS_cover.jpg)
## Overview

J.A.R.V.I.S is a personal assistant that can - 

- automate tasks on your computer
- Give daily reports of your computer usage, internet usage, etc.
- schedule tasks to be completed at other times
- Uses AI-generated speech to talk
- Listens to your voice using Google Speech API

## Log

v0.3 - Finally! Speech Recognition works! It's because I forgot to change mic settings in... settings. Also added answers to conversational questions like how are you, etc. Also opens up more apps (File Explorer and Calculator to be precise). Still need to fix internet searches (they have sort of been screwed thanks to speech recognition). Need to add - 

- Calc functions to JARVIS
- Weather API (to gather info about weather)
- Close apps (currently, it can only open them)
- create reports (health reports, usage reports, inspired by iOS' Screen Usage report)
- Scheduler and inbuilt timetable
- A GUI for JARVIS (similar to most personal AI assistants like Siri and Google, etc.)
- Export the JARVIS assistant as .exe for easier installation
- Automation of multiple tasks at once (e.g. - 'Open microsoft word, then search "how to write a story" using chrome')
- File Manipulation (e.g. open, read, write, edit and save files)
- Wake Detection for JARVIS (e.g. 'Hey JARVIS!')
- Database filled with answers to questions used in conversational speech (not a necessity)
- Recommendations (health recommendations, weather recommendations, etc.)
- Email Manipulation (Able to open, read, write, edit and send emails. This is not a necessity)

## In Depth

JARVIS is currently (v0.2) split into 4 components, the `app_opener`, which handles app opening, `web_searches`, which manages web searches, the `command_handler`, which relays command inputed by the user to functions inside the `app_opener` and `web_searches` module and finally the `main.py` (for v0.2 it's called `test.py`), which combines the three modules together and actually runs JARVIS.

```Python

print('Thanks for Reading!')

```

