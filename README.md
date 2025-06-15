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

[Choc v1 switches](https://www.kailh.net/products/kailh-choc-v2-low-profile-switch-set)

[USB-C connector](https://www.digikey.com/en/products/detail/gct/USB4105-GF-A/11198441)

[Diodes](https://www.digikey.com/en/products/detail/mcc-micro-commercial-components/1N4148W-TP/717196)

[Electrostatic protection](https://www.digikey.com/en/products/detail/umw/usblc6-2sc6/16705896)

One USB-C data cable to communicate between halves and one more to communicate to the computer.

### Additional tools

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
