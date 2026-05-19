import machine
import time

# Xiao RP2040
csn = machine.Pin(1, machine.Pin.OUT)
clk = machine.Pin(2, machine.Pin.OUT)
do = machine.Pin(4, machine.Pin.IN)

INC = 1
DEC = 2

# Initialize states
csn.value(1) # CSn High (Inactive)
clk.value(1)

# The raw 16-bit packet: [Angle(10bit) | OCF | COF | LIN | DEC | INC | PAR]
def decode(data, ones):

    # Extract 10-bit angle (bits 15-6)
    angle = (data >> 6) & 0x03FF

    # magnet not detected if INC and DEC are high
    mag = (data >> INC) and (data >> DEC)
    
    # even parity
    err = (ones % 2) != 0

    return angle, mag, err

def read_as5040_data():
    # CSn low to start transfer
    csn.value(0)
    time.sleep_us(2)
    
    # Read 16 bits (Data + Status)
    data = 0
    ones = 0
    for i in range(16):
        clk.value(0)
        time.sleep_us(1)
        clk.value(1)
        time.sleep_us(1)
        bit = do.value()
        ones = ones + bit
        data = (data << 1) | bit
    
    # CSn high to end transfer
    csn.value(1)

    return data, ones
    
def read_as5040():
    while True:
        data, ones = read_as5040_data()
        angle, mag, err = decode(data, ones)
        if err:
            print('Parity error')
        else:
            break
    return angle, mag


# Main loop
while True:
    try:
        angle, mag = read_as5040()
        
        if not mag:
            print("Magnet not detected")
        else:
            # Convert 0-1023 to 0-359 degrees
            degrees = (angle * 360) / 1024
            print(f"Raw: {angle}, Angle: {degrees:.2f} deg")
            
    except Exception as e:
        print("Error:", e)
        
    time.sleep(0.1)

