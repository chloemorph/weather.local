# weather.local

This Raspberry Pi projects creates a IoT API for Pimoroni's [Enrivo pHat](https://shop.pimoroni.com/products/enviro-phat), versioned with [Dat](https://github.com/datproject/dat). The API is accessible at `http://weather.local/index.json`, the sensor data is recorded through the Dat History, accessible with `http://weather.local/index.json/?version=10`.

## Create the SD Card

Install [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/) and use [Etcher](https://etcher.io/) burn it on a SD Card.

## Setup WIFI and SSH

### SSH

Insert the SD Card, and create a file named `ssh`.

`touch /Volumes/boot/ssh`

### WIFI

Create a new file named `wpa_supplicant.conf`.

```
touch /Volumes/boot/wpa_supplicant.conf
nano /Volumes/boot/wpa_supplicant.conf
```

#### Network Settings

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
  ssid="<network_name>"
  psk="<network_password>"
}
```

## Setup Basics

### Connect to the device

The device's password should be `raspberry`.

```
ssh pi@raspberrypi.local
```

### Setup

Activate both "Interface/SSH", and "Advanced/Expand FS".

```
sudo raspi-config
```

### Reboot

```
sudo reboot
```

### Update

```
sudo apt-get update
sudo apt-get upgrade
```

### Rename

```
sudo nano /etc/hostname
sudo nano /etc/hosts
```

## Setup Server

### Install NPM

```
wget https://nodejs.org/dist/v8.11.1/node-v8.11.1-linux-armv7l.tar.xz
tar xvf ./node-v8.11.1-linux-armv7l.tar.xz
cd node-v8.11.1-linux-armv7l/bin
sudo cp ./node /usr/bin/
sudo ./npm install npm@latest -g
sudo npm update
```

### Install Dat

```
sudo npm install dat -g
```

### Install Forever

```
sudo npm install forever -g
```

### Redirect incoming to Dat port

```
sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
```

## Setup API

### Cron

Added the scheduled tasks with `crontab -e`.

```
*/5 * * * * sudo python ~/weather.local/record.py
```

### Start API
```
cd ~
git clone https://github.com/hundredrabbits/weather.local.git
cd weather.local/
forever start ./serve.js
```

This is the source code for the **Pino** [Weather Station](https://wiki.xxiivv.com/#weather+station). 

