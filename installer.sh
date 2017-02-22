#!/bin/bash
# Installer for weather application.
apt-get update
apt-get upgrade
apt-get install python-dev
apt-get install python-usb
pip install pywws
echo 'Testing weather station link - should show a lot of numbers.'
python -m pywws.TestWeatherStation
addgroup --system weather
adduser pi weather
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
python setup.py install
