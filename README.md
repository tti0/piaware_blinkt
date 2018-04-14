# piaware_blinkt
A Python script to show the status of PiAware visually using a Pimoroni Blinkt on a Raspberry Pi.

## License
This project is licensed under the terms of the MIT License. See the file https://github.com/tti0/piaware_blinkt/blob/master/LICENSE for full terms.

This work is copyright 2018 tti0 (https://github.com/tti0).

## About
If you have a Raspberry Pi, running the flight tracking software PiAware (https://flightaware.com/adsb/piaware/), by navigating to the web server on the Raspberry Pi, one can view the status of four different parts of PiAware: **Radio**, **PiAware**, **FlightAware** and **MLAT**. On the web server, the status of these can be **red**, **yellow** or **green**. These colours are replicated on the LEDs of the Pimoroni Blinkt (https://shop.pimoroni.com/products/blinkt), an inexpensive (~ 5GBP / 6USD) LED add-on board for the Raspberry Pi. The table below shows the use of each LED on the Blinkt board. LEDs are numbered in the table as in the official Blinkt Python library.

| LED # | Use                                                            |
|-------|----------------------------------------------------------------|
| 0     | "Radio" status from web sever (RED/YELLOW/GREEN)               |
| 1     | "PiAware" status from web server (RED/YELLOW/GREEN)            |
| 2     | "FlightAware" status from web server (RED/YELLOW/GREEN)        |
| 3     | "MLAT" status from web server (RED/YELLOW/GREEN)               |
| 4     | Not used (ALWAYS OFF)                                          |
| 5     | Not used (ALWAYS OFF)                                          |
| 6     | CPU temperature indicator (RED/YELLOW/GREEN - see table below) |
| 7     | Power indicator (ALWAYS WHITE)                                 |

For the CPU indicator, the colour to temperature correlation is as follows:

| CPU temperature, t (°C) | Colour |
|--------------------------------------|--------|
| t ≥ 90                               | Red    |
| 90 > t ≥ 75                          | Yellow |
| 75 > t                               | Green  |

*90°C is the absolute maximum rated CPU temperature for a Raspberry Pi. You should manually shut your Raspberry Pi down if the CPU Temperature indicator LED turns red.**

The system is made up from two parts `grab.sh` and `piaware_blinkt.py`. `grab.sh` loads the latest status from PiAware every 2 seconds as JSON data, using `curl`. `piaware_blinkt.py` is a Python script which interprets the data from JSON, loads in the latest CPU temperature and sets the LEDs accordingly.

## Setup Instructions
