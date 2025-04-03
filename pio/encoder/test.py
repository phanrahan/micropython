import time
from machine import Pin
from encoder import Encoder

# Test with encoder on pins 1 and 2:
pin1 = Pin(1,Pin.IN, Pin.PULL_UP)
pin2 = Pin(2,Pin.IN, Pin.PULL_UP)

e = Encoder(1, pin1)

while True:
  time.sleep(0.1)
  print(e.value())

