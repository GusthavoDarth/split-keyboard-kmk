print("Starting r")

import board
from kmk.modules.split import Split, SplitType, SplitSide

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

split = Split(
    split_type=SplitType.UART,
    data_pin=board.GP0,
    data_pin2=board.GP1,
    use_pio=True
    )
keyboard.modules.append(split)

keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.GP23,
    board.GP22,
    board.GP21,
    board.GP20,
    board.GP19,
    board.GP18,
)
keyboard.row_pins = (board.GP14, board.GP15, board.GP16, board.GP17)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

TOP = KC.MO(1)															
LOWER = KC.MO(2)


keyboard.keymap = [
    [
        KC.TAB,     KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,            KC.Y,    KC.U,     KC.I,     KC.O,     KC.P,        KC.BKDL,
        KC.LCTRL,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,            KC.H,    KC.J,     KC.K,     KC.L,     KC.SCLN,     KC.QUOT,
        KC.LSHIFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,            KC.N,    KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,     KC.ESC,
        KC.NO,      KC.NO,    KC.NO,    KC.LGUI,  TOP,      KC.SPACE,        KC.ENTER,LOWER,    KC.LALT,  KC.NO,    KC.NO,       KC.NO,
    ],

    [
        KC.TAB,     KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,         KC.CIRC, KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,     KC.DEL,
        KC.LCTRL,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,           KC.N6,   KC.N7,    KC.N8,    KC.N9,    KC.N0,       KC.NO,
        KC.LSHIFT,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,           KC.LBRC, KC.RBRC,  KC.MINS,  KC.EQL,   KC.NO,       KC.NO,
        KC.NO,      KC.NO,    KC.NO,    KC.LGUI,  KC.TRANS, KC.SPACE,        KC.ENTER,KC.TRANS, KC.LALT,  KC.NO,    KC.NO,       KC.NO,
    ],
    
    [
        KC.TAB,     KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,           KC.NO,   KC.NO,    KC.NO,    KC.NO,    KC.NO,       KC.NO,
        KC.LCTRL,   KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,           KC.NO,   KC.UP,    KC.NO,    KC.NO,    KC.NO,       KC.NO,
        KC.LSHIFT,  KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,           KC.LEFT, KC.DOWN,  KC.RIGHT, KC.NO,    KC.NO,       KC.NO,
        KC.NO,      KC.NO,    KC.NO,    KC.LGUI,  KC.TRANS, KC.SPACE,        KC.ENTER,KC.TRANS, KC.LALT,  KC.NO,    KC.NO,       KC.NO,
    ],

]

if __name__ == "__main__":
    keyboard.go()

    