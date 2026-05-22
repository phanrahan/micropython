# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

MicroPython driver for the AS5048A 14-bit magnetic rotary encoder, targeting the Xiao RP2040 board. Communication is via SPI.

## Running on Hardware

```bash
ampy run as5048.py
```

`ampy` (Adafruit MicroPython tool) uploads and runs the script on the connected microcontroller over USB serial.

## Hardware Configuration

- **Board**: Xiao RP2040
- **Interface**: SPI(0) at 1 MHz, polarity=0, phase=1, 8-bit mode
- **Pins**: SCK=2, MOSI=3, MISO=4, CS=1

## AS5048A Protocol

The sensor uses a 16-bit SPI frame:
- Bit 15: even parity (currently disabled/commented out)
- Bit 14: R/W flag (1 = read)
- Bits 13–0: register address or angle data

The sensor returns the angle from the **previous** command (pipelined). The 14-bit angle value (0–16383) maps to 0–360°. Bit 14 of the response is an error flag (weak magnetic field or device error).

## Current Status

Work in progress. Parity calculation is implemented but disabled (lines 28–29). The SPI was recently switched from 16-bit to 8-bit mode with manual byte splitting in `write_readinto`.
