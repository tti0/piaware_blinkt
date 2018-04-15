#!/bin/bash
while true
do
    curl -s http://localhost/status.json > /home/pi/piaware_blinkt/status.json
    sleep 2
done
