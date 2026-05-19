from machine import Pin, SPI
import time

# Xiao RP2040
spi = SPI(1, baudrate=1000000, polarity=1, phase=1, bits=16,
          sck=Pin(2), mosi=Pin(3), miso=Pin(4))
cs = Pin(1, Pin.OUT, value=1) # Chip Select pin

# AS5048A Constants
AS5048_CMD_READ_ANGLE = 0x3FFF

def calculate_parity(command):
    """Calculates even parity for the 16-bit command."""
    count = 0
    for i in range(16):
        if (command >> i) & 0x01:
            count += 1
    return count % 2

def read_angle():
    # Construct the 16-bit read command
    # Bit 14: R/W (1 for Read)
    # Bit 15: Parity (calculated below)
    command = AS5048_CMD_READ_ANGLE | 0x4000
    parity = calculate_parity(command)
    command = command | (parity << 15)
    
    # SPI Transaction
    cs.value(0)
    time.sleep_us(1) # Minimum 350ns CS to CLK setup time
    
    # Send command and simultaneously read response
    # (The AS5048 replies with the angle from the *previous* command)
    rx_data = bytearray(2)
    spi.write_readinto(bytearray([(command >> 8) & 0xFF, command & 0xFF]), rx_data)
    
    cs.value(1)
    
    # Combine the two returned bytes
    result = (rx_data[0] << 8) | rx_data[1]
    
    # Check if the error flag (bit 14) is set in the returned data
    if (result & 0x4000):
        print("Device Error or Weak Magnetic Field!")
    
    # Mask out the top 2 bits (Parity and Error Flag) to get the 14-bit angle
    angle = result & 0x3FFF
    return angle

# --- Main Loop ---
while True:
    raw_val = read_angle()
    # Convert 14-bit raw value (0-16383) to degrees (0-360)
    angle_degrees = (raw_val / 16383.0) * 360.0 
    
    print(f"Raw: {raw_val} | Angle: {angle_degrees:.2f}°")
    time.sleep_ms(100)

