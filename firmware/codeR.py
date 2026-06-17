import board
from keymap import keymap
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.scanners import DiodeOrientation

print("Starting right half")

keyboard = KMKKeyboard()

# Lado direito eh o peripheral: GP0/GP1 = UART TX/RX para o lado esquerdo.
split = Split(
    split_type=SplitType.UART,
    data_pin=board.GP0,
    data_pin2=board.GP1,
    use_pio=True,
)
keyboard.modules.append(split)
keyboard.modules.append(Layers())

# Matriz 4 rows x 6 cols (metade direita, colunas em ordem espelhada
# em relacao ao lado esquerdo). Diodos orientados col->row.
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

keyboard.keymap = keymap

keyboard.go()
