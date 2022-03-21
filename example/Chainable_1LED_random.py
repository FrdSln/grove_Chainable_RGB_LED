# exemple pour une DEL chainable
from microbit import *
import random
import mb_ChainableLED_grove

DEL = mb_grove_ChainableLED.ChainableLED_grove(pin16, pin15, 1)

while True:
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    print(R, G, B)
    DEL.setColorRGB(0, R, G, B)
    sleep(2000)
