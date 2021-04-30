#Blynk code for Project4 "Mood Meter"

import json
import time
import blynklib
from urllib.request import urlopen
from sense_hat import SenseHat
from faces import normal, sad, happy

#Personal authentication key for Blynk and Thingspeak
BLYNK_AUTH = '<BLYNK AUTHENTICATION KEY HERE>'
TS_API_KEY = '<THINGSPEAK API KEY HERE>'

#Thingspeak API URL
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % TS_API_KEY

sense = SenseHat()
sense.clear()
mood = '0'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

#Physical mood input on pi
while True:
        for event in sense.stick.get_events():
                if event.action == "pressed":
                        if event.direction == "up":
                                print('feeling ok :|')
                                sense.set_pixels(normal)
                        elif event.direction == "left":
                                print('feeling good :)')
                                sense.set_pixels(happy)
                        elif event.direction == "right":
                                print('feeling bad :(')
                                sense.set_pixels(sad)
                                
#set your current mood by adjusting the slider.
#output will be sent to the senseHat
#output will also be sent to a channel on Thingspeak
@blynk.handle_event('write V1')
def write_vp3_slider(pin, value):
        global mood
        print('V1:' + str(value))
        mood = str(value[0])
        if int(value[0]) == 0:
                print('feeling good :)')
                sense.set_pixels(happy)
        elif int(value[0]) == 1:
                print('feeling ok :|')
                sense.set_pixels(normal)
        elif int(value[0]) == 2:
                print('feeling bad :(')
                sense.set_pixels(sad)
        else:
                sense.clear(255,255,255)

# register handler for virtual pin V2(temperature) reading
@blynk.handle_event('read V0')
def read_virtual_pin_handler(pin):
    temp=round(sense.get_temperature(),2)
    print('V0 Read: ' + str(temp))
    blynk.virtual_write(pin, temp)
    writeData(temp)
        
#thingspeak code
def writeData(temp):
        global mood
        URL = baseURL + '&field1=%s&field2=%s' % (str(mood),str(temp))
        print(URL)
        conn = urlopen(baseURL + '&field1=%s&field2=%s' % (str(mood),str(temp)))
        print(conn.read())
        conn.close()

# infinite loop that waits for event
while True:
        blynk.run()
