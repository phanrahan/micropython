# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

MicroPython drivers for AMS magnetic rotary encoder ICs, intended to run directly on microcontrollers (RP2040, ESP32, etc.).

- `as5040.py` — bit-banged SPI driver for the AS5040 (10-bit resolution). Uses raw GPIO pins (CSn, CLK, DO) with manual clock toggling. Returns angle (0–1023), magnet status, and error flag.
- `as5048.py` — hardware SPI driver for the AS5048A (14-bit resolution). Uses MicroPython's `machine.SPI` with parity-checked 16-bit commands. Returns angle (0–16383).

## Hardware Setup

**AS5040** (bit-bang SPI, RP2040 pin defaults):
- CSn → GPIO 17
- CLK → GPIO 18
- DO  → GPIO 16

**AS5048A** (hardware SPI, ESP32 VSPI defaults):
- SCK → GPIO 18, MOSI → GPIO 23, MISO → GPIO 19
- CS  → GPIO 5

## Deployment

Copy the relevant `.py` file to the board with any MicroPython file transfer tool (e.g., `ampy`, `rshell`, Thonny). The scripts run as standalone programs with a `while True` main loop — paste into the REPL or save as `main.py`.

```bash
# Example using ampy (see ../ampy/)
ampy --port /dev/ttyUSB0 put as5040.py main.py
```

## Key Implementation Notes

- **AS5040 SPI timing**: clock idles high, data captured on falling edge; 1 µs delays between transitions.
- **AS5048A protocol**: each SPI transaction returns the response to the *previous* command (pipeline). The angle read command must include a read/write bit (bit 14) and even parity (bit 15).
- Both scripts contain hardcoded pin numbers at module level — change these constants before deploying to a different board.
