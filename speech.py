from gtts import gTTS
import os

myText="text to speech conversation"
language ='en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
