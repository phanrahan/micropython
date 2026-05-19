import math
import array
from machine import Pin, I2S

# 1. Initialize I2S with XIAO RP2040 Pins
SCK_PIN = 2  # D2
WS_PIN = 3   # D3
SD_PIN = 4   # D4

# Setup for RX (Input)
audio_in = I2S(
    0, 
    sck=Pin(SCK_PIN), 
    ws=Pin(WS_PIN), 
    sd=Pin(SD_PIN), 
    mode=I2S.RX, 
    bits=16, 
    format=I2S.MONO, 
    rate=16000
)

# Read audio data
mic_data = bytearray(1024)
num_read = audio_in.readinto(mic_data)
