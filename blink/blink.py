from machine import Pin
import time

# pico and pico2
led_pin = 25 

# xiao rp2040
#led_pin = 17 # R  
#led_pin = 16 # G  
#led_pin = 25 # B

# esp32c3
#led_pin = 10  

led = Pin(led_pin, Pin.OUT)
while 1:
  led.on()
  time.sleep_ms(500)
  led.off()
  time.sleep_ms(500)
