from machine import Pin, I2C
import sh1106

# using default address 0x3C
i2c = I2C(1, sda=Pin(6), scl=Pin(7))

display = sh1106.SH1106_I2C(128, 64, i2c)
display.flip(True)

display.fill(0)
#display.fill_rect(0, 0, 128, 64, 0)
display.text('Hello, World!', 0, 0, 1)
display.show()
