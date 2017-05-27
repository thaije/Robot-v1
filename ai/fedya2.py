
from gtts import gTTS
from pygame import mixer
from time import sleep

tts = gTTS(text='Nice booty you got there', lang='ru')
tts.save('hello.mp3')

print "translated"
sleep(5)

print 'speaking'

# play audio
mixer.init()
mixer.music.load('hello.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()

