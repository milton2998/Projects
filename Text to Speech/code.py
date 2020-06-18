from gtts import gTTS
import os





# add text in the file if needed
# f = open('text_for_speech.txt')



print("Write the text here : ")
x = input()
language = 'en'

audio = gTTS(text=x,lang=language)
audio.save('generated_audio.wav')

os.system('vlc --play-and-exit generated_audio.wav')
