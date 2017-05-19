# Tjalling Haije
# 25/01/2016
# Write a sentence to a text file, a jar file reads it in and
# converts it to a mp3 with an tts vocalizer. Then play the mp3.

import subprocess
from pygame import mixer

# input txt file and write text to it
file = open("tss-input.txt", "w")
file.write("Hello Sophie, I am Fedya! How are you doing? You good looking tiger. Rawr")
file.close()

# call the tts jar file and convert to mp3
subprocess.call(['java', '-jar', 'tts/tts.jar'])


# Play the mp3 file and sleep for length of file
mixer.init()
mixer.music.load('speech.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()


