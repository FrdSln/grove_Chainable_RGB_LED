# exemple pour trois DELs chainables
from microbit import *
import random
import mb_grove_ChainableLED

DEL = mb_grove_ChainableLED.ChainableLED_grove(pin16, pin15, 3)

while True:
    for i in range(3):
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        DEL.setColorRGB(i, R, G, B)

    sleep(500)
