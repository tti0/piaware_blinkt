# piaware_blinkt
A Python script to show the status of PiAware visually using a Pimoroni Blinkt on a Raspberry Pi.

<img src="https://s31.postimg.cc/7s59cbl9n/piaware_demo.jpg" width="30%" />

*Demo above: I've added a sheet of paper with LED descriptors to my clear Raspberry Pi case.*

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

| CPU temperature, t (°C)              | LED colour |
|--------------------------------------|------------|
| t ≥ 90                               | Red        |
| 90 > t ≥ 75                          | Yellow     |
| 75 > t                               | Green      |

*90°C is the absolute maximum rated CPU temperature for a Raspberry Pi. You should manually shut your Raspberry Pi down if the CPU temperature indicator LED turns red.*

The system is made up from two parts `grab.sh` and `piaware_blinkt.py`. `grab.sh` loads the latest status from PiAware every 2 seconds as JSON data, using `curl`. `piaware_blinkt.py` is a Python script which interprets the data from JSON, loads in the latest CPU temperature and sets the LEDs accordingly.

Note that the Blinkt LEDs will remain on after system shutdown, for as long as the power supply is connected the the Raspberry Pi.

## Setup Instructions

### Pre-requisites
- Your Raspberry Pi has an internet connection.

### Setup
*For all steps in this guide, answer "Yes" or "Y" if prompted by the Linux shell.*

1. If you have not done so already, set up PiAware on your Raspberry Pi. Follow the instructions in the links below if you have not. There are two possible ways to set up PiAware.
  1. Use the PiAware SD card image: https://flightaware.com/adsb/piaware/build (step 2 of this guide)
  2. Set up PiAware on a standard Raspbian installation: https://flightaware.com/adsb/piaware/install

2. Gain access to the shell of your Raspberry Pi as the user `pi`. To do this, you can either connect to the Raspberry Pi using SSH (https://www.raspberrypi.org/documentation/remote-access/ssh), or connect a keyboard and monitor to the Raspberry Pi. If you are using the PiAware SD card image, the default password for the `pi` user is `flightaware`. For Raspbian, the default password for the `pi` user is `raspberry`.

3. Install the Pimoroni Blinkt Python library. Follow Pimoroni's instructions at https://github.com/pimoroni/blinkt to do so.

4. Ensure you are in the `pi` user home directory. To do this, enter the command:
```
cd ~
```

5. Update your packages and repositories with the command:
```
sudo apt-get update && sudo apt-get upgrade
```

6. Install `git` on the Raspberry Pi with command:
```
sudo apt-get install git
```

7. Grab the latest version of the `piaware_blinkt` code with the command:
```
git clone https://github.com/tti0/piaware_blinkt
```

8. Add execute permissions to the code files with the commands:
```
sudo chmod 777 piaware_blinkt/grab.sh
```
and
```
sudo chmod 777 piaware_blinkt/piaware_blinkt.py
```

9. Now we will make th Raspberry Pi automatically start the `piaware_blinkt` script on startup. Open `/etc/rc.local` with the command:
```
sudo nano /etc/rc.local
```

10. In `nano`, use the arrow keys to the line above `exit 0`, and add the following code:
```
/home/pi/piaware_blinkt/grab.sh &
sleep 5
sudo /usr/bin/python /home/pi/blinkt-status/piaware_blinkt.py > /dev/null 2>&1 &
```

11. Ensure that the line `exit 0` is still present.

12. Save your changes, with the keyboard shortut `Ctrl + O`, and then type `Y` to confirm the save.

13. Press `Ctrl + X` to exit `nano`.

14. Reboot the Raspberry Pi with the command:
```
sudo reboot
```

15. You are now finished. The LEDs should come on when the Raspberry Pi boots.
