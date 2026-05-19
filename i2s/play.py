import math
import array
from machine import Pin, I2S

# 1. Initialize I2S with XIAO RP2040 Pins
SCK_PIN = 2  # D2
WS_PIN = 3   # D3
SD_PIN = 4   # D4

audio_out = I2S(
    0,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mode=I2S.TX,
    bits=16,
    format=I2S.STEREO,
    rate=44100,
    ibuf=10000,
)

# 2. Generate a sine wave buffer
SAMPLE_RATE = 48000
TONE_FREQ = 1000  # 1000 Hz sine wave
length = SAMPLE_RATE // TONE_FREQ
samples = array.array("h", [0] * length)

for i in range(length):
    # generate 16-bit sine wave values
    samples[i] = int(32767 * math.sin(2 * math.pi * i / length))

# 3. Play the tone continuously
while True:
    audio_out.write(samples)
