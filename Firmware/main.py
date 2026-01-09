import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, SSD1306

# ─────────────────────────────
# Keyboard instance
# ─────────────────────────────
keyboard = KMKKeyboard()

# ─────────────────────────────
# Switches (7 direct GPIO pins)
# Matches your schematic exactly
# ─────────────────────────────
PINS = (
    board.A0,   # GPIO26 - SW1
    board.A1,   # GPIO27 - SW2
    board.A2,   # GPIO28 - SW3
    board.A3,   # GPIO29 - SW4
    board.TX,   # GPIO0  - SW5
    board.RX,   # GPIO1  - SW6
    board.SCK,  # GPIO2  - SW7
)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # switch shorts to GND
)

# ─────────────────────────────
# Rotary Encoder (A/B only)
# GPIO3 and GPIO4 per schematic
# ─────────────────────────────
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.MOSI, board.MISO),  # GPIO3, GPIO4
)

# Clockwise / Counter-clockwise
encoder.map = [
    ((KC.VOLD, KC.VOLU),)
]

# ─────────────────────────────
# OLED Display (SSD1306 128x32)
# I²C on GPIO6 / GPIO7
# ─────────────────────────────
oled = Display(
    display=SSD1306(
        i2c_bus=1,
        sda=board.D4,  # GPIO6
        scl=board.D5,  # GPIO7
        width=128,
        height=32,
    ),
)

keyboard.extensions.append(oled)

# ─────────────────────────────
# Keymap (7 keys = 7 switches)
# ─────────────────────────────
keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.E,
        KC.F,
        KC.G,
    ]
]

# ─────────────────────────────
# Start KMK
# ─────────────────────────────
keyboard.go()
