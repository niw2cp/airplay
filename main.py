#!/usr/bin/env python
import os, random

played = 1

import pyttsx3
def readfile(file):
    engine = pyttsx3.init()
    #file = "readthis.txt"
    fileo = open(file, "r" )
    lines_of_text = fileo.readlines() 
    engine.say(lines_of_text)
    engine.runAndWait()
    
file = "readthis.txt"


def rndmp3 ():
    global played
    randomfile = random.choice(os.listdir("OnAir/"))
    file = ' /home/pi/Mainlist/'+ randomfile
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
