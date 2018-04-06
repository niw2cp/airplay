#!/usr/bin/env python
import os, random

played = 1

def rndmp3 ():
   global played
   randomfile = random.choice(os.listdir("/home/pi/Music/"))
   file = ' /home/pi/Mainlist/'+ randomfile
   if file == played:
    pass
   else:
    print file
    os.system ('omxplayer -o local' + file)    
    played = file

while True:
 rndmp3 ()
fi
done
