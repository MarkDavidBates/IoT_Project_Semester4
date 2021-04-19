#Blynk code for Project4 "Mood Meter"

import blynklib
from sense_hat import SenseHat
from faces import normal, sad, happy

#Personal authentication key for Blynk
BLYNK_AUTH = 'vcIWMN9GL2XKoyJn9cclkl2Q_Rwx8knN'

sense = SenseHat()
sense.clear()

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

#set your current mood by adjusting the slider.
#output will be sent to the senseHat
#output will also be sent to a channel on Thingspeak
@blynk.handle_event('write V3')
def write_vp3_slider(pin, value):
        print('V3:' + str(value))
        if int(value[0]) == 0:
                #sense.clear(0,0,255)
                print('feeling good :)')
                sense.set_pixels(happy)
        elif int(value[0]) == 1:
                #sense.clear(255,200,0)
                print('feeling ok :|')
                sense.set_pixels(normal)
        elif int(value[0]) == 2:
                #sense.clear(255,0,0)
                print('feeling bad :(')
                sense.set_pixels(sad)
        else:
                sense.clear(255,255,255)


# infinite loop that waits for event
while True:
        blynk.run()
