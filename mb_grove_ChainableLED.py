# Chainable LED V1.0 pour microbit
# Connexion sur P16 (clk) et P15 (data)

from microbit import *
import time

class ChainableLED_grove():
    # initialisation : broches utilisées - nombre de leds
    def __init__(self, clk_pin, data_pin, number_of_leds):
        self.clk_pin = clk_pin
        self.data_pin = data_pin
        self.number_of_leds = number_of_leds
        self.led_state = [0] * number_of_leds * 3
        for i in range(number_of_leds):
            self.setColorRGB(i, 0, 0, 0)

    def clk(self):
        self.clk_pin.write_digital(0)
        time.sleep_us(20)
        self.clk_pin.write_digital(1)
        time.sleep_us(20)

    def sendByte(self, b):
        for i in range(8):
            if ((b & 0x80) != 0):
                self.data_pin.write_digital(1)
            else:
                self.data_pin.write_digital(0)
            self.clk()
            b = b << 1

    def sendColor(self, red, green, blue):
        prefix = 0b11000000
        if ((blue & 0x80) == 0):
            prefix |= 0b00100000
        if ((blue & 0x40) == 0):
            prefix |= 0b00010000
        if ((green & 0x80) == 0):
            prefix |= 0b00001000
        if ((green & 0x40) == 0):
            prefix |= 0b00000100
        if ((red & 0x80) == 0):
            prefix |= 0b00000010
        if ((red & 0x40) == 0):
            prefix |= 0b00000001
        self.sendByte(prefix)

        self.sendByte(blue)
        self.sendByte(green)
        self.sendByte(red)

    # définit les valeurs RGB de la led choisie
    def setColorRGB(self, led, red, green, blue):
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)

        for i in range(self.number_of_leds):
            if (i == led):
                del self.led_state[i*3]
                self.led_state.insert(i*3, red)
                del self.led_state[i*3+1]
                self.led_state.insert(i*3+1, green)
                del self.led_state[i*3+2]
                self.led_state.insert(i*3+2, blue)

            self.sendColor(self.led_state[i*3],self.led_state[i*3+1],self.led_state[i*3+2])

        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
