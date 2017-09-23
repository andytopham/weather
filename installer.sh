#!/bin/bash
# Installer for weather application.
apt-get -y update
apt-get -y upgrade
apt-get -y install python-dev
apt-get -y install python-usb
pip install pywws
echo 'Testing weather station link - should show a lot of numbers.'
python -m pywws.TestWeatherStation
addgroup --system weather
adduser pi weather
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
python setup.py install
cd ..
# Adafruit LCD drivers
sudo apt-get install build-essential python-dev python-smbus python-pip git
sudo pip install RPi.GPIO
# Add to autostart
cp myweather.service /lib/systemd/system
chmod 644 /lib/systemd/system/myweather.service
systemctl daemon-reload
systemctl enable myweather.service
echo "Now need to reboot"
# To check whether it is running....
# sudo systemctl status myweather.service
