from eeprom import EEPROM
from machine import I2C, Pin

I2C_ADDR = 0x50     # DEC 80, HEX 0x50
EEPROM_SIZE = 32    # AT24C32 on 0x50

# define custom I2C interface, default is 'I2C(0)'
# check the docs of your device for further details and pin infos
i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=800000)
eeprom = EEPROM(addr=I2C_ADDR, at24x=EEPROM_SIZE, i2c=i2c)

# write 'micropython' to address 10
eeprom.write(10, 'micropython')

# read 11 bytes starting at address 10
eeprom.read(10, 11)

# update content at address 10 with 'MicroPython'
# only changed values are written, here 'm' -> 'M' and 'p' -> 'P'
eeprom.write(10, 'MicroPython')
