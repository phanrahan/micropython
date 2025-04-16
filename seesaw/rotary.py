"""
`adafruit_seesaw.rotaryio`
====================================================
"""

_ENCODER_BASE = const(0x11)

_ENCODER_STATUS = const(0x00)
_ENCODER_INTENSET = const(0x10)
_ENCODER_INTENCLR = const(0x20)
_ENCODER_POSITION = const(0x30)
_ENCODER_DELTA = const(0x40)

class IncrementalEncoder:
    """IncrementalEncoder determines the relative rotational position based
    on two series of pulses."""

    def __init__(self, seesaw, encoder=0):
        """Create an IncrementalEncoder object associated with the given
        eesaw device."""
        self._seesaw = seesaw
        self._encoder = encoder

    @property
    def position(self):
        """The current position in terms of pulses. The number of pulses per
        rotation is defined by the specific hardware."""
        return self._seesaw.encoder_position(self._encoder)

    @position.setter
    def position(self, value):
        self._seesaw.set_encoder_position(value, self._encoder)

    def encoder_position(self, encoder=0):
        """The current position of the encoder"""
        buf = bytearray(4)
        self._seesaw_read(_ENCODER_BASE, _ENCODER_POSITION + encoder, buf)
        return struct.unpack(">i", buf)[0]

    def set_encoder_position(self, pos, encoder=0):
        """Set the current position of the encoder"""
        cmd = struct.pack(">i", pos)
        self._seesaw_write(_ENCODER_BASE, _ENCODER_POSITION + encoder, cmd)

    def encoder_delta(self, encoder=0):
        """The change in encoder position since it was last read"""
        buf = bytearray(4)
        self._seesaw_read(_ENCODER_BASE, _ENCODER_DELTA + encoder, buf)
        return struct.unpack(">i", buf)[0]

    def enable_encoder_interrupt(self, encoder=0):
        """Enable the interrupt to fire when the encoder changes position"""
        self._seesaw_write8(_ENCODER_BASE, _ENCODER_INTENSET + encoder, 0x01)

    def disable_encoder_interrupt(self, encoder=0):
        """Disable the interrupt from firing when the encoder changes"""
        self._seesaw_write8(_ENCODER_BASE, _ENCODER_INTENCLR + encoder, 0x01)
