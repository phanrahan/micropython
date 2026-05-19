import machine
import time

# Xiao RP2040
csn = machine.Pin(1, machine.Pin.OUT)
clk = machine.Pin(2, machine.Pin.OUT)
do = machine.Pin(4, machine.Pin.IN)

# Initialize states
csn.value(1) # CSn High (Inactive)
clk.value(1) # Clock High

def read_as5040():
    # CSn low to start transfer
    csn.value(0)
    time.sleep_us(1)
    
    # Read 16 bits (Data + Status)
    data = 0
    ones = 0
    for i in range(16):
        clk.value(0)
        time.sleep_us(1)
        bit = do.value()
        ones = ones + bit
        data = (data << 1) | bit
        clk.value(1)
        time.sleep_us(1)
    
    # CSn high to end transfer
    csn.value(1)
    
    # Extract 10-bit angle (bits 15-6)
    # The raw 16-bit packet: [Angle(10bit) | MAG | DEC | INC | PAR | ERR]
    angle = (data >> 6) & 0x03FF
    
    # Extract status bits
    err = ones != 0
    mag = (data >> 4) and (data >> 3)
    
    return angle, mag, err

# Main loop
while True:
    try:
        angle, mag, err = read_as5040()
        
        if err:
            print("Parity error detected!")
        elif not mag:
            print("Magnet missing/weak")
        else:
            # Convert 0-1023 to 0-359 degrees
            degrees = (angle * 360) / 1024
            print(f"Raw: {angle}, Angle: {degrees:.2f} deg")
            
    except Exception as e:
        print("Error:", e)
        
    time.sleep(0.1)

