#!/usr/bin/env python
import os, random

played = 1
current_dir = os.path.dirname(__file__)

import re
import pyttsx3

def readfile(file, voice_type=0):
    engine = pyttsx3.init()
    if (voice_type == 1):
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[1].id)  
   
    #file = "readthis.txt"
    fileo = open(file, "r" )
    lines_of_text = fileo.readlines()
    lines_of_text = re.sub(r'\\n', '. ', str(lines_of_text))
    engine.say(lines_of_text)
    engine.runAndWait()

file = "readthis.txt"
readfile(file,1)

def rndmp3 ():
    global played
    global current_dir
    randomfile = random.choice(os.listdir("OnAir/"))
    file = current_dir + randomfile
    if file == played:
        pass
    
    elif randomfile.endswith('.txt'):
        readfile(file)
        #print(randomfile)
 
    else:
        print(randomfile)
        os.system ('omxplayer -o local' + file)    
        played = file

while True:
    rndmp3 ()
fi
done
