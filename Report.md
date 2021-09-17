# EC463 Fall 2021 Hardware Miniproject Team #11
By Ismaeel AlAlawi (ENG '22) and Laith Shamieh (ENG '22).

## Data Collection
Using SSH to control the Raspberry Pi 4B remotely(connected to hotspot), we ran our modified ble_scan.py code to detect bluetooth devices in an area on the Boston University campus:
- Data logging started at 2:45 pm on Saturday September 11th, 2021. 
- Location: George Sherman Union (GSU), in the dining area in front of the Market, next to the last column in front of the boundary wall separating the supermarket and the dining area
- Five entries lasting 1 minute each with a 1 minute interval in between 
- First entry @ 2:45 pm, second entry @ 2:47 pm, third entry @ 2:49 pm, fourth entry @ 2:51 pm, and fifth entry @ 2:53 pm.
- All bluetooth devices detected were recorded and stored in a text file "hw11_miniproj_data.txt"

## Data Analysis
After acquiring data from "ble_scan.py" which outputs it into a text file "hw11_miniproj_data.txt", we wrote the python code "ble_analysis.py" which reads the text file and removes the duplicates from the file then summing all the lines up and subtracting 1 (because of the "Scanning BLE devices for 60 seconds" line) to get the total number of people during a 10-minute period. This code also outputs a modified file "hw11_miniproj_data_modified.txt" with no duplicates. 

Aside from using our "ble_analysis.py" code to analyze the data, it is also possible to use the following direct shell command on the original raw .txt file to confirm the python script is working as intended. 

```
sort hw11_miniproj_data.txt | uniq -d
```
This shell command will sort the data, remove duplicates accordingly – the same way "ble_analysis.py" does – and display the results on the terminal. Thus, it is also expected that if you run it on the modified .txt file, it will not show anything on the command line because all the non-duplicates have been removed using the python script. To test that out, simply use the aforementioned command on "hw11_miniproj_data_modified.txt". 

## Conclusion
In conclusion of this Raspberry Pi data collection experiment, the python script yields a total number of 466 people (assuming that every person has one bluetooth device in order to have a 1:1 ratio of BLE scanned devices to people) within a 10-minute period. Obviously, we know that this ratio in reality is larger due to the ubiquity of technology today – especially on a college campus, you'd expect a student to carry several bluetooth devices, hence this rough approximation is surely an overestimate but provides a good enough qualitative measure for the purposes of the miniproject. 
