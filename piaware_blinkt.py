# piaware_blinkt.py - A Python script to show the status of PiAware visually using a Pimoroni Blinkt on a Raspberry Pi
# Author: tti0

#!/usr/bin/env python

import colorsys
import time
import blinkt
import json

blinkt.set_brightness(0.04)

blinkt.set_all(255,0,255)
blinkt.show()
time.sleep(30)
blinkt.set_all(0,0,0)
blinkt.show()
time.sleep(2)

def loadin():
    global cpuf
    cpuf = open("/sys/class/thermal/thermal_zone0/temp","r")
    global cput
    cput = int(cpuf.read())/1000

    with open('status.json') as json_data:
        d = json.load(json_data)
        global piaware
        piaware = str((d["piaware"]))
        global mlat
        mlat = str((d["mlat"]))
	global flightaware        
	flightaware = str((d["adept"]))
        global radio
        radio = str((d["radio"]))

def whiteon():
    blinkt.set_pixel(7,120,120,200)
    blinkt.show()

def statled(led, col):
    if col == 0: #ok
        blinkt.set_pixel(led,0,255,0)
    elif col == 1: #warning
        blinkt.set_pixel(led,20,10,0)
    elif col == 2: #error
        blinkt.set_pixel(led,150,0,0)
    blinkt.show()

#led 0 radio
#led 1 piaware
#led 2 flightaware
#led 3 mlat
#led 6 temp
#led 7 power

def main():
    print("reload")
    whiteon()
    loadin()
    print(cput)

    if 'green' in radio:
        statled(0,0)
    elif 'amber' in radio:
        statled(0,1)
    elif 'red' in radio:
        statled(0,2)

    if 'green' in piaware:
        statled(1,0)
    elif 'amber' in piaware:
        statled(1,1)
    elif 'red' in piaware:
        statled(1,2)

    if 'green' in flightaware:
        statled(2,0)
    elif 'amber' in flightaware:
        statled(2,1)
    elif 'red' in flightaware:
        statled(2,2)

    if 'green' in mlat:
        statled(3,0)
    elif 'amber' in mlat:
        statled(3,1)
    elif 'red' in mlat:
        statled(3,2)

    if cput > 90:
        statled(6,2)
    elif cput > 75:
        statled(6,1)
    else:
        statled(6,0)

    time.sleep(5)
    loadin()


loadin()
while True:
    try:
        print("Try run")
	main()
    except:
        print("Except run")
        time.sleep(3)
        main()
