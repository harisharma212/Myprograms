import random
from gtts import gTTS 
import os 
  

# Language in which you want to convert 
language = 'en'

number_list = random.sample(range(1, 91), 90)

notation = {'1': 'st', '2': 'nd', '3': 'rd'}

i = 0
text = 'Welcome to Housy... Lets start\n\n'
while(i<90):
	text += '%s%s Number is: %s\n' % (i+1, notation.get(str(i+1)[-1], 'th'), number_list[i])
	i += 1

myobj = gTTS(text=text, lang=language, slow=False) 
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("/home/welcome.mp3")