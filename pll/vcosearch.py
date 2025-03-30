MHZ = 1000000

XOSC_HZ = 12 * MHZ
PLL_SYS_REFDIV = 1
reference_freq = XOSC_HZ // PLL_SYS_REFDIV

PICO_PLL_VCO_MIN_FREQ = 750* MHZ
PICO_PLL_VCO_MAX_FREQ = 1600* MHZ

def vco(fbdiv):
    return reference_freq * fbdiv

def freq(fbdiv, postdiv1, postdiv2):
    return vco(fbdiv) / (postdiv1 * postdiv2)

def search(exact=True):
    print( 'exact' if exact else 'inexact')
    for fbdiv in range(320,16-1,-1):
        vco = fbdiv * reference_freq
        if vco < PICO_PLL_VCO_MIN_FREQ or vco > PICO_PLL_VCO_MAX_FREQ:
            continue
        for postdiv1 in range(7,0,-1):
            for postdiv2 in range(postdiv1,0,-1):
                if exact and vco % (postdiv1 * postdiv2) != 0:
                    continue
                out = vco / (postdiv1 * postdiv2)
                yield (fbdiv, postdiv1, postdiv2)
    return None

#divider = 65536
for param in search(False):
    f = freq(*param)
    if f >= 125_000_000 and f <= 135_000_000:
        #print(f, f/divider, param)
        print(f, param)
