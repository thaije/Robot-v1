# Tjalling Haije
# 25/01/2016
# Write a sentence to a text file, a jar file reads it in and
# converts it to a mp3 with an tts vocalizer. Then play the mp3.

import subprocess
from tts import vlc
import os.path
import time
from mutagen.mp3 import MP3

# input txt file and write text to it
file = open("tss-input.txt", "w")
file.write("Hello Tsjalling, I am Fedya! How are you doing? You cyka")
file.close()

# call the tts jar file and convert to mp3
subprocess.call(['java', '-jar', 'tts/tts.jar'])

# Play the mp3 file and sleep for length of file
length = MP3("speech.mp3").info.length
path = os.path.abspath(os.path.join("speech.mp3", os.pardir))
path =  path.replace(" ", "")
p = vlc.MediaPlayer("file://" + path + "/speech.mp3")

# play track and set volume
p.play()
time.sleep(0.01)
p.audio_set_volume(125)
time.sleep(length)

