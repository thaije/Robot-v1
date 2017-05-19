
from gtts import gTTS
from pygame import mixer


tts = gTTS(text='Hello', lang='en', slow=True)
tts.save('hello.mp3')

# play audio
mixer.init()
mixer.music.load('speech.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()