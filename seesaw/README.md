# SeeSaw MicroPython Drivers

o seesaw
- https://learn.adafruit.com/adafruit-seesaw-atsamd09-breakout/overview
- https://github.com/adafruit/Adafruit_CircuitPython_seesaw/tree/main/adafruit_seesaw

## Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor
https://www.adafruit.com/product/4026

Copy the following files to your board:
- `seesaw.py`
- `stemma_soil_sensor.py`

Usage:
```
SDA_PIN = 23 # update this
SCL_PIN = 22 # update this

i2c = machine.I2C(sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)
seesaw = StemmaSoilSensor(i2c)

# get moisture
moisture = seesaw.get_moisture()

# get temperature
temperature = seesaw.get_temp()
```

Pico I2C slave
- https://github.com/ifurusato/rp2040-i2c-slave
