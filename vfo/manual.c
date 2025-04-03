*
* set_freq_manual(uint64_t freq, uint64_t pll_freq, enum si5351_clock clk)
*
* Sets the clock frequency of the specified CLK output using the given PLL
* frequency. You must ensure that the MS is assigned to the correct PLL and
* that the PLL is set to the correct frequency before using this method.
*
* It is important to note that if you use this method, you will have to
* track that all settings are sane yourself.
* 
* freq - Output frequency in Hz
* pll_freq - Frequency of the PLL driving the Multisynth in Hz * 100
* clk - Clock output
*   (use the si5351_clock enum)
*
def set_freq_manual(self, freq : int, pll_freq : int, clk : int):
	int_mode = 0
	div_by_4 = 0

	# Lower bounds check
	if freq > 0 and freq < _CLKOUT_MIN_FREQ * _FREQ_MULT:
		freq = _CLKOUT_MIN_FREQ * _FREQ_MULT

	# Upper bounds check
	if freq > _CLKOUT_MAX_FREQ * _FREQ_MULT:
		freq = _CLKOUT_MAX_FREQ * _FREQ_MULT

	self.clk_freq[clk] = freq

	self.set_pll(self.pll_freq, self.pll_assignment[clk])

	self.output_enable(clk, 1)

	r_div = self.select_r_div(&freq)

	# Calculate the synth parameters
	multisynth_calc(freq, pll_freq, &ms_reg)

	# If freq > 150 MHz, we need to use DIVBY4 and integer mode
	if freq >= _MULTISYNTH_DIVBY4_FREQ * _FREQ_MULT:
		div_by_4 = 1
		int_mode = 1

	# Set multisynth registers (MS must be set before PLL)
	self.set_ms(clk, ms_reg, int_mode, r_div, div_by_4)

    return 0
