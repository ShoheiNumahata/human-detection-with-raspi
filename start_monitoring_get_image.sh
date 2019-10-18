#!/bin/sh
while true
do
	/usr/bin/python3 /home/pi/monitoring_get_image.py

	sleep 20
	/bin/date
done
