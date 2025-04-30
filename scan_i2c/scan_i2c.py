from machine import Pin, I2C

# xiao RP2040
# i2c = I2C(1, sda=Pin(6), scl=Pin(7))

# rp2040 zero
i2c = I2C(1, sda=Pin(26), scl=Pin(27))

devices = i2c.scan()
print("devices: ")
for device in devices:
    print("0x{0:02x}".format(device))
