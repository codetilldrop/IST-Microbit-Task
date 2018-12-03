# Author: Dillon de Silva

from microbit import *
import radio

text_to_scroll = "hi"

radio.on()
display.show(Image.SAD)
# CONNECTED_DEVICES is a variable which holds
# the number of connected devices
CONNECTED_DEVICES = 0

# Recognising devices which are going to connect
while button_a.was_pressed() == False:
  connection_message = radio.receive()
  if connection_message == 'connected':
    CONNECTED_DEVICES += 1

display.show(Image.HAPPY)
# Scrolling letter by letter across a series of microbits
for letter in text_to_scroll: 
  for i in range(0, CONNECTED_DEVICES + 2):
    radio.config(channel=i)
    radio.send(letter)
    sleep(750)