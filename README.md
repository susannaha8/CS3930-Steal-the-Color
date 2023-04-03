
# Creative Embedded Systems: Interactive Devices

For our module 1 installation, we used an ESP32 TTGO display, a joystick, and a button to create our own interactive designs. I chose to use PyGame, a python library, to create a visual display that responds to various inputs from my hardware device. Click here for artistic documentation:


## Setting up the Hardware

This project consists of a breadboard, 7 wires, and three main pieces of hardware: an ESP32, a joystick, and a button. Plug the pins of the hardware into the breadboard, and connected them further with wires: connect the joystick to the ESP32 with one wire to Ground, one to 3V, and the other three to pins 25, 26, and 27 for X, Y, and Z motion; connect the button with one wire to Ground, and the other to pin 13 for digital input. The ESP32 is powered via a USBC cable.


## Flashing Code to the ESP32

After setting up our hardware, used the code found in `src/main.cpp` to recieve serial input from the joystick and the button. Change the pin numbers if you used different GPIO pins. You can either write this code in the Arduino application or through the VSCode IDE PlatformIO. Set the port to serial input, and set the baudrate to match whatever you value you put in your  `src/main.cpp` code (ex. `Serial.begin(115200);`.) To do this in PlatformIO, in `platformio.ini`, add a line like `monitor_speed = 115200`. 

## Reading Serial Input


## Creating My Display with PyGame


