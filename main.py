#!/usr/bin/env python
import os, random

played = 1

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
