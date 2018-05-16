#!/usr/bin/env python
import os, random

log = 0 #default = 0
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

def playlog(file):
    if(log == 1):
        global current_dir
        new_dir = current_dir+"/playlog"
        if(os.path.isfile(new_dir)):
          print("1")
          pass
        else:
          os.makedirs(new_dir)
          print(new_dir)

        if(os.path.isfile(new_dir+"/playlog.txt")):
          fh = open(new_dir+"/playlog.txt", "a")
        else:
          fh = open(new_dir+"/playlog.txt", "x")

        output_text = "file"

        #print(output_text)
        fh.writelines(output_text)
        fh.close()


def rndmp3 ():
    global played
    global current_dir
    randomfile = random.choice(os.listdir("OnAir/"))
    file = current_dir + randomfile
    if file == played:
        pass
    
    elif randomfile.endswith('.txt'):
        readfile(file)
        playlog(randomfile)
 
    else:
        playlog(randomfile)
        os.system ('omxplayer -o local' + file)    
        played = file

while True:
    rndmp3 ()
fi
done
