XOSC_HZ = 12 * MHZ
PLL_SYS_REFDIV = 1
PICO_PLL_VCO_MIN_FREQ_HZ 750* MHZ
PICO_PLL_VCO_MAX_FREQ_HZ 1600* MHZ

bool check_sys_clock_hz(uint32_t freq_hz, uint *vco_out, uint *postdiv1_out, uint *postdiv2_out) {
    uint reference_freq_hz = XOSC_HZ / PLL_SYS_REFDIV;
    for (uint fbdiv = 320; fbdiv >= 16; fbdiv--) {
        uint vco_hz = fbdiv * reference_freq_hz;
        if (vco_hz < PICO_PLL_VCO_MIN_FREQ_HZ || vco_hz > PICO_PLL_VCO_MAX_FREQ_HZ) continue;
        for (uint postdiv1 = 7; postdiv1 >= 1; postdiv1--) {
            for (uint postdiv2 = postdiv1; postdiv2 >= 1; postdiv2--) {
                uint out = vco_hz / (postdiv1 * postdiv2);
                if (out == freq_hz && !(vco_hz % (postdiv1 * postdiv2))) {
                    *vco_out = vco_hz;
                    *postdiv1_out = postdiv1;
                    *postdiv2_out = postdiv2;
                    return true;
                }
            }
        }
    }
    return false;
}
