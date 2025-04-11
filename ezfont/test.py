from machine import Pin, I2C
import sh1106
from ezFBfont import ezFBfont
from sys import path

path.append('fonts')
import ezFBfont_spleen_12x24_ascii_23
import ezFBfont_spleen_16x32_num_26

# For RP2040 Xiao use pins 7 and 6 for I2C bus 1
i2c = I2C(1, sda=Pin(6), scl=Pin(7))

oled = sh1106.SH1106_I2C(128, 64, i2c)
oled.flip()

# spleen_12x24_ascii_23 : initialised: height: 23, fixed width: 12, baseline: 18
# font1 = ezFBfont(oled, ezFBfont_spleen_12x24_ascii_23, tkey=0, verbose=True)
# spleen_16x32_num_26 : initialised: height: 26, fixed width: 16, baseline: 23
font1 = ezFBfont(oled, ezFBfont_spleen_16x32_num_26, tkey=0, verbose=True)

#font1.write('Hello', 0, 0)
#font1.write('0123456789', 0, 0)
font1.write('7000000', 0, 0)

oled.show()

while True:
    pass


