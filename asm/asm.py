import time
from rp2 import PIO, asm_pio
from machine import Pin
import array

# Define the blink program.  It has one GPIO to bind to on the set instruction, which is an output pin.
# Use lots of delays to make the blinking visible by eye.
@asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1) [4]    
    set(pins, 0) [4]   
    wrap()

# Instantiate a state machine with the blink program, at 1000Hz, with set bound to Pin(25) (LED on the rp2 board)
sm = rp2.StateMachine(0, blink, freq=100000000, set_base=Pin(15))

# test assembler and
# implement 'addressof'
a=array.array('i',[ 1, 2, 3])
# invoke assembler
@micropython.asm_thumb
# passing an array name to the assembler
# actually passes in the address
def addressof(r0):
    # r0 is the output register, so address beomes output
    mov(r0, r0)
# now use the assembler routine  
addr_a = addressof(a)
print(addr_a)
print(machine.mem32[addressof(a)+8]) # returns '3'

# Run the state machine for 3 seconds.  The LED should blink.
sm.active(1)
time.sleep(3)
sm.active(0)
sm = rp2.StateMachine(0, blink, freq=50000000, set_base=Pin(15))
sm.active(1)
time.sleep(3)
sm.active(0)
