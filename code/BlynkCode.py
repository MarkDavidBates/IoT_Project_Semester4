#Blynk code for Project4 "Mood Meter"

import blynklib
from sense_hat import SenseHat

#Personal authentication key for Blynk
BLYNK_AUTH = 'vcIWMN9GL2XKoyJn9cclkl2Q_Rwx8knN'

sense = SenseHat()
sense.clear()

green = (0,255,0)
orange = (255,165,0)
red = (255,0,0)

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
                sense.show_message(':)', text_colour = green)
        elif int(value[0]) == 1:
                #sense.clear(255,200,0)
                print('feeling ok :|')
                sense.show_message(':|', text_colour = orange)
        elif int(value[0]) == 2:
                #sense.clear(255,0,0)
                print('feeling bad :(')
                sense.show_message(':(', text_colour = red)
        else:
                sense.clear(255,255,255)


# infinite loop that waits for event
while True:
        blynk.run()
