"""
Reads and edit text files to remove any lines that are duplicates & prints number of lines (devices) that are unique
Example of analyzing scanned Bluetooth Low Energy (BLE) device data from ble_scan.py.
Reference: newbedev.com
"""

lines_seen = set() # create empty set to hold lines already seen 

# finds the duplicate lines, and deletes them from the .txt file
with open('hw11_miniproj_data_modified.txt', 'r+') as f:
    d = f.readlines() 
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            print(i)
            lines_seen.add(i)
    f.truncate()
    
    # sum up the number of lines in the modified .txt file which contains
    # unique BLE IDs, and subtract one since "Scanning..." is one of them
    # and is not counted as a person
    num_lines = sum(1 for line in open('hw11_miniproj_data_modified.txt')) - 1
    print("Number of people = " + str(num_lines)) 
    f.close()
    
