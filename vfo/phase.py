from machine import Pin, I2C
import si5351

# For RP2040 Xiao use pins 7 and 6 for I2C bus 1
i2c = I2C(1, sda=Pin(6), scl=Pin(7))

si5351 = si5351.SI5351(i2c)

def main():
    si5351.init(si5351.CRYSTAL_LOAD_8PF, 0, 0)

    # We will output 14.1 MHz on CLK0 and CLK1.
    # A PLLA frequency of 705 MHz was chosen to give an even
    # divisor by 14.1 MHz.
    freq = 1410000000
    pll_freq = 70500000000

    # Set CLK0 and CLK1 to output 14.1 MHz with a fixed PLL frequency
    si5351.set_freq_manual(freq, pll_freq, SI5351_CLK0)
    si5351.set_freq_manual(freq, pll_freq, SI5351_CLK1)

    # Now we can set CLK1 to have a 90 deg phase shift by entering
    # 50 in the CLK1 phase register, since the ratio of the PLL to
    # the clock frequency is 50.
    si5351.set_phase(SI5351_CLK0, 0)
    si5351.set_phase(SI5351_CLK1, 50)

    # We need to reset the PLL before they will be in phase alignment
    si5351.pll_reset(SI5351_PLLA)

    while True:
        pass

main()
