#!/usr/bin/env python3
"""
Example of scanning Bluetooth Low Energy (BLE) devices.
Requires a Linux computer due to gattlib underlying BLE scanning requiring Glib.
"""

import argparse
from bluetooth.ble import DiscoveryService

p = argparse.ArgumentParser(description="BLE scanner")
p.add_argument(
    "timeout",
    help="number of seconds to scan for BLE devices",
    nargs="?",
    type=int,
    default=5,
)
P = p.parse_args()

timeout = P.timeout

print(f"Scanning BLE devices for {timeout} seconds")

f = open("hw11_miniproj_data.txt", "a")
f.write(f"Scanning BLE devices for {timeout} seconds" + '\n')

for u, n in ble_devs.items():
    tup = (u,n)
    print(u, n)
    f.write(''.join(tup) + '\n') 
 
f.close()
