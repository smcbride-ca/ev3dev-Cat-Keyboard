# ev3dev-Cat-Keyboard
The code for a Lego Mindstorms EV3 cat treat dispenser, controlled by a keyboard. This was made for the ev3dev operating system, and MIGHT work with ev3 micropython. (No guarantees)
# Setup
First, the `keyboard` module is needed, and can be installed using `pip3 install keyboard`. 
The program needs to be run as root, due to the limitations of the keyboard module. The easiest way to do this (without the start script) is plugging in a keyboard and pressing CTRL+ALT+F6 to enter terminal. Then you can use `cd` to navigate to the directory your file is in, and use `sudo python3 cat_keyboard.py` to start the program.
Using the start script is a much easier way to start the program.
