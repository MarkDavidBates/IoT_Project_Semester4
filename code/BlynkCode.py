#Blynk code for Project4 "Mood Meter"

import json
import time
import blynklib
from urllib.request import urlopen
from sense_hat import SenseHat
from faces import normal, sad, happy

#Personal authentication key for Blynk and Thingspeak
BLYNK_AUTH = 'vcIWMN9GL2XKoyJn9cclkl2Q_Rwx8knN'
TS_API_KEY = '4UJI1HS1VXFU2MUC'

#Thingspeak API URL
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % TS_API_KEY

sense = SenseHat()
sense.clear()

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

#set your current mood by adjusting the slider.
#output will be sent to the senseHat
#output will also be sent to a channel on Thingspeak
@blynk.handle_event('write V1')
def write_vp3_slider(pin, value):
        print('V1:' + str(value))
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

# infinite loop that waits for event
while True:
        blynk.run()
