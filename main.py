#!/usr/bin/env python
import os, random
from lxml import etree

played = 1
def read_forecast():
   file = open('forecast.xml')
   tree = etree.parse(file)
   timename = tree.xpath('//data/time-layout/start-valid-time/@period-name')
   cast = tree.xpath('//wordedForecast/text/text()')
   forecast = timename[0],"it's", cast[0], timename[1], "will be", cast[1]
   engine = pyttsx3.init()
   engine.say(forecast)
   engine.runAndWait()

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
