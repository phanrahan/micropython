import time
from machine import I2C, Pin
from eeprom import EEPROM

I2C_ADDR = 0x50     # HEX 0x50
EEPROM_SIZE = 512   # AT24C512

# For RP2040 Xiao use pins 7 and 6 for I2C bus 1
# i2c = I2C(1, sda=Pin(6), scl=Pin(7))

# rp2040 zero
i2c = I2C(1, sda=Pin(26), scl=Pin(27))

eeprom = EEPROM(addr=I2C_ADDR, at24x=EEPROM_SIZE, i2c=i2c)

while True:
    # write 'micropython' to address 10
    eeprom.write(10, 'micropython')

    # read 11 bytes starting at address 10
    print(eeprom.read(10, 11))

    time.sleep(1)
