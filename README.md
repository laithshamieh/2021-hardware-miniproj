# 2021 Hardware Miniproject

Fall 2021 ECE Senior Capstone miniproject

This project will be done in multiple steps.
The first part is the setup of the Raspberry Pi hardware.

The second part is an exercise to gain familiarity with Python and embedded sensors. It will require the Raspberry Pi OS to be working.

The third part is using the Raspberry Pi as a wireless sensor with WiFi and/or Bluetooth.

## Part 1: setup Raspberry Pi

The Raspberry Pi requires the students obtain a micro-SD card and install the Raspberry Pi OS.
8GB or larger micro SD card recommended--these days, 32 GB is often the minimum size one finds commonly available.
An 32GB micro SD UHS-1 card is about $5 from:

* Microcenter (730 Memorial Drive, Cambridge--just across BU Bridge)
* Amazon
* many other places

The Raspberry Pi OS is a freely available fork of Debian customized for the Raspberry Pi.
To install the OS, the student team will need to
[download the OS image](https://www.raspberrypi.org/software/)
via the installer to the SD card.
Please use care that the installer refers to the path to the SD card.
If your computer doesn't have a micro SD slot, consider buying an inexpensive USB to micro SD adapter or using another computer.

Notes:

* if you have trouble with the laptop crashing while writing or verifying the SD card, try temporarily turning off virus protection, especially on Windows.
* The Raspberry Pi 4 uses more power than prior generations. It might not operate correctly if powered from laptop USB-C. We suggest using the Raspberry Pi 4 AC power adapter for stable power.

We have setup a few HDMI displays and USB keyboards in the senior design lab to share.
Please let us know if we need to add more.

### SSH connection

To connect to the Raspberry Pi over SSH do one of the following connection methods.
Be sure to pick a strong password for the Raspberry Pi, or the Pi will quickly become hacked as university networks are aggressively scanned for low security passwords.

#### external HDMI display

Type "raspi-config" in the Pi terminal, "Interface Options", "SSH" enable.
Then similarly setup the WiFi network, to your phone or laptop WiFi hotspot or the university Guest WiFi network.
If using guest network, you'll need to login to the WiFi network with a web browser from the Pi.

#### no display, via Ethernet cable to laptop

Create a blank file named "ssh" in the "boot" partition of the SD card while it's in your laptop.
This is done on Linux or MacOS from the "boot" directory by "touch ssh" or on Windows PowerShell by "New-Item ssh"
To enable WiFi, create a file in the "boot" directory of the SD card
[wpa_supplicant.conf](https://www.raspberrypi.org/documentation/configuration/wireless/wpa_supplicant.md)
with the needed WiFi parameters (country code is "US").

Example wpa_supplicant.conf:

```init
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
        ssid="myHomeNetwork"
        psk="abc123"
}

network={
        ssid="MyPhoneHotspot"
        psk="xyz789"
}
```

---

To connect to the Raspberry Pi over SSH while plugged into the Pi with an Ethernet cable from your laptop or on the same WiFi network, type the following in the terminal:

```sh
ssh pi@raspberrypi.local
```

If you can't connect, ensure your computer is connected to the Raspberry Pi via Ethernet cable directly.
For example, on Windows type "ipconfig" and the response should include:

```
> ipconfig

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : <hex-address>
   Autoconfiguration IPv4 Address. . : 169.254.57.200
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . :
```

The last digits will be different, the important part is the "169.254" indicating you have a "link-local" connection active.

If you still can't get it working, use an HDMI display and keyboard to the Pi, which can be easier to get started when there's a connection problem.

### Internet connection

To enable the WiFi internet connection, from "raspi-config", "System Options", "Wireless LAN" setup the WiFi network.
Note that if you choose to use university WiFi, your Kerberos password is visible to anyone with access to the Pi.
Additional ways to connect the Pi to the internet include:

* Ethernet cable to an internet-connected wall jack
* WiFi hotspot

You can check that the Pi is on the internet by typing in the Pi terminal (over SSH or HDMI+keyboard):

```sh
curl https://ident.me
```

that will give the public IP address of the Pi, if the public internet connection is up.

### Python setup

The commands in this section are all run on the Raspberry Pi, over SSH or HDMI+keyboard.
Let's update the Raspberry Pi OS, as the OS releases only happen a few times a year.

```sh
sudo apt update && sudo apt upgrade
```

Like most Linux systems, the Raspberry Pi comes with Python installed.
Since we're going to be using system hardware drivers, we'll use system Python.
Check that Python is working:

```sh
$ python3

Python 3.7.3  ...
```

Most contemporary Python software requires Python &ge; 3.7 at this time.

## Part 2: Python exercise

You can try the Bluetooth [ble_scan.py](./ble_scan.py) and/or WiFi examples [wifi_scan.py](./wifi_scan.py) in this project on the Raspberry Pi.

I have made notes for [Bluetooth](./Bluetooth.md) as it requires additional packages.

## Part 3: Wireless Sensor

Let's examine the possibility of detecting automobile, bicycle, and/or pedestrian activity in an area.
Many people carry smartphones or have automobiles that beacon with Bluetooth.
While more precise tracking requires multiple Bluetooth receivers, just using one Bluetooth receiver in our Raspberry Pi can give a sense of user activity in an area.

What would you like to measure via Bluetooth activity in an area using a Raspberry Pi?
Ideas include:

* room occupancy trends
* traffic patterns (congestion of automobiles, bikes, and/or pedestrians)

Let discuss in class on Thursday, September 9, 2021 your ideas.
Each team could measure something a little different if they choose.

### General approach

Consider using a for loop to scan for BLE devices.
The [wifi_scan.py](./wifi_scan.py) example shows a way to log data to a JSON file over time, near the bottom of the Python script.
You'll find that some devices are always visible--they are probably fixed beacons, TVs, speakers, desktop computers, etc.
Devices like headphones, modern automobiles, etc. come and go as they move close to and away from the Raspberry Pi.

An issue with automobiles is not every modern automobile beacons BLE after its paired, or may only beacon during user setup interactions.
Let's use WiFi hotspots for detecting vehicles instead.

### WiFi hotspot detection in automobiles

Automobile hotspots have a specified range typically up to about 20 meters from the vehicle.
We are close enough to the road to be able to detect the vehicle WiFi hotspot as they travel past.
A typical WiFi beacon interval is 100 milliseconds.

The
[iw wireless toolkit](https://wireless.wiki.kernel.org/en/users/documentation/iw)
is available on many Linux systems including the Raspberry Pi OS.
We use this tool and parse its output in [wifi_scan.py](./wifi_scan.py) to detect WiFi hotspots, such as exist in modern automobiles.

```sh
sudo python3 wifi_scan.py ~/data -N 100
# logs data to ~/data and scans 100 times
```

copy this file to your laptop, perhaps using
[SCP](https://en.wikipedia.org/wiki/Secure_copy_protocol):

```sh
scp pi@raspberrypi.local:~/data/*.json .
```

---

Note, if you wish to measure/do something else with the Pi, please let us know and we'll discuss.
