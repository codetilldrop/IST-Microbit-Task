# Author: Dillon de Silva

from microbit import *
import radio

radio.on()

VALID_CHARS = ['a', 'b',
    'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z']

while True:
    # Sending connectivity message
    if button_a.was_pressed():
        radio.send('connected')
        break

radio.config(channel=2)
while True:
    message = radio.receive()
    if message in VALID_CHARS:
        display.scroll(message)