# CowPi
A water level indicator for Raspberry Pi. Designed to be used on a cow trough.
The 3rd and 6th GPIO pins are used to connect a simple float switch.
This is set up for a NO float switch, but simply reversing the button states in the code would enable it for a NC switch 

The Pi this was initially designed for is housed in a remote cow pasture that has access to a 5G wifi hotspot for connectivity. 

EDIT 8/4/2021
-Added logging function in which a txt file is created and/or edited to record each switch status check with a time stamp
-Added a second process "CowLogger" to record each change in switch status with a time stamp in a txt file
-Added a file that enables running both scripts in a single call out with a subprocess.run function

