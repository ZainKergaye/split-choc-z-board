# Choc split-key z-board

The choc split key zboard is another ergonomic split-keyboard designed for comfort and efficiency. Using wired USB-C connectors to communicate between halves, it is a plain simple keyboard.

> [!CAUTION]
> This project is being redone! I chose the wrong board that does not support UART!

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Hardware](#hardware)
5. [Firmware Installation and Configuration](#firmware-installation-and-configuration)
6. [Assembly](#assembly)
7. [Troubleshooting](#troubleshooting)

## Features

- Ergonomic split design for improved comfort
- Custom PCB with SMD and THC components
- Open-source firmware using [QMK](https://docs.qmk.fm).
- 3D printed [case](https://www.printables.com/@ZainKergaye_241410)

## Getting Started

To make your own keyboard order all the parts in the [hardware](#hardware) section. Solder
everything according to the silkscreen, be prepared to solder SMD and THC components. 3D
print the case. Build and flash the firmware. Then you are done!

## Hardware

### PCB

Order the PCB from any manufacurer you want, the exported gerbers are below.

[Left half gerbers](./split-choc-z-board/gerbers/left-half-gerbers.zip)

### Components

[Choc v1 switches](https://www.amazon.com/dp/B0BLC9BKW8)

[Keycaps](https://www.amazon.com/dp/B0D2DCDBSW)

[QSPI Flash](https://www.digikey.com/en/products/detail/winbond-electronics/W25Q128JVSIQ-TR/5803944)

[RP2040](https://www.digikey.com/en/products/detail/raspberry-pi/SC0914-13/14306010?s=N4IgTCBcDaIE4AcwAYAsyQF0C%2BQ)

[Button](https://www.digikey.com/en/products/detail/e-switch/TL3315NF250Q/1870396)

[Resistor 10k](https://www.digikey.com/en/products/detail/bourns-inc/CR0603-FX-1002ELF/3593188)

[Resistor 27.4k](https://www.digikey.com/en/products/detail/bourns-inc/CR0603-FX-27R4ELF/3783905)

[Resistor 4.99k](https://www.digikey.com/en/products/detail/bourns-inc/CR0603-FX-4991ELF/2345092)

[Resistor 1k](https://www.digikey.com/en/products/detail/bourns-inc/CR0603-JW-102ELF/3741004)

[Capacitor 15pf](https://www.digikey.com/en/products/detail/murata-electronics/GCM1555C1H150JA16D/4903554)

[Capacitor 10uf](https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL05A106MQ5NUNC/3887109)

[Capacitor 1uf](https://www.digikey.com/en/products/detail/taiyo-yuden/JMK105BJ105KV-F/930583)

[Capacitor 0.1uf](https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL05B104KP5NNNC/3886660)

[USB-C connector](https://www.digikey.com/en/products/detail/gct/USB4105-GF-A/11198441)

[Diodes](https://www.digikey.com/en/products/detail/mcc-micro-commercial-components/1N4148W-TP/717196)

[Electrostatic protection](https://www.digikey.com/en/products/detail/umw/usblc6-2sc6/16705896)

One USB-C data cable to communicate between halves and one more to communicate to the computer.

### Additional tools

- Hot air soldering station / Reflow oven
- Soldering iron
- Solder wire
- Solder paste (For SMD)
- Rosin

## Firmware Installation and Configuration

Currently a work in progress...

## Assembly

Currently a work in progress...

## Troubleshooting

If you have encountered any problems or issues, feel free to create an issue [here](https://github.com/ZainKergaye/split-choc-z-board/issues)!
