# Split Keyboard

A handmade 42-key split mechanical keyboard built around two Raspberry Pi Picos running [KMK firmware](https://github.com/KMKfw/kmk_firmware) in MicroPython. The case was sculpted by hand using air-dry clay.

![Split Keyboard](./hardware/image5.webp)

## Hardware

| Component | Details |
|---|---|
| Controller | Raspberry Pi Pico (×2) |
| Switches | Akko Fairy Silent (×42) |
| Layout | 21 keys per half |
| Connection | USB-C (wired split) |
| Case | Hand-sculpted air-dry clay |

## Firmware

Runs [KMK](https://github.com/KMKfw/kmk_firmware), a feature-rich keyboard firmware written in MicroPython. KMK handles split communication over UART, layers, and key mapping with minimal boilerplate.

## Build Notes

The case was the most unconventional part of this build — sculpted from air-dry clay, shaped around the switch plate, and left to cure.

Each half uses a Raspberry Pi Pico flashed with CircuitPython + KMK. The two halves communicate over a USCB-C cable. Key matrix is hand-wired.

## Flashing

1. Flash CircuitPython onto both Picos ([download](https://circuitpython.org/board/raspberry_pi_pico/))
2. Copy the KMK source onto each Pico's filesystem
3. working in progress


## Repository Structure

```
.
├── firmware/
│   working in progress
│   
├── images/
│   └── keyboard images
└── README.md
```

## License

MIT
