import uasyncio as asyncio
from machine import Pin, I2S

# 1. Setup I2S Devices
# Shared pins (BCLK, WS)
bck_pin = Pin(26)
ws_pin = Pin(27)

# Microphone (Input)
sdin_pin = Pin(28)
audio_in = I2S(
    0, 
    sck=bck_pin, 
    ws=ws_pin, 
    sd=sdin_pin, 
    mode=I2S.RX, 
    bits=16, 
    format=I2S.MONO, 
    rate=16000
)

# Speaker/Amplifier (Output)
sdout_pin = Pin(29)
audio_out = I2S(
    1, 
    sck=bck_pin, 
    ws=ws_pin, 
    sd=sdout_pin, 
    mode=I2S.TX, 
    bits=16, 
    format=I2S.MONO, 
    rate=16000
)

# 2. Async Routines
async def record_and_play():
    # Buffer to hold microphone data (chunk size)
    chunk_size = 512
    in_buffer = bytearray(chunk_size)
    
    print("Starting simultaneous record and play...")
    
    while True:
        # Read a chunk from the microphone
        num_bytes_read = audio_in.readinto(in_buffer)
        
        # If data is successfully read, play it back immediately
        if num_bytes_read > 0:
            # You can also apply DSP (like a volume boost or filter) to 'in_buffer' here
            audio_out.write(in_buffer)
            
        # Give control back to the event loop
        await asyncio.sleep_ms(0)

# 3. Main Event Loop
async def main():
    task = asyncio.create_task(record_and_play())
    await asyncio.gather(task)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Stopped.")
    audio_in.deinit()
    audio_out.deinit()
