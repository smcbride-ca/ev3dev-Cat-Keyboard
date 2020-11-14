#!/usr/bin/env python3

#Import the needed modules.
#Time for getting the time and waiting, LargeMotor for motor control,
# Leds for the leds, Sound for audio, and keyboard for input.
import time
from ev3dev2.motor import LargeMotor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
import keyboard

#Set up commands
lm = LargeMotor()
leds = Leds()
sound = Sound()

#Turn all lights off
leds.all_off()

#BEEP and then get user input on the number of rotations the motor will do.
#The "Try" part trys to run that command
#The "except" part is what runs if there is an error
#The "finally" part is what happens after.
sound.beep()
try:
    rot = int(input("Rotation: "))
except:
    print("\rThere was an error. Please try again.")
    rot = float(input("Rotation: "))
finally:
    print("Rotation set successfully")

#Set time variables
curtime = (time.time())
time.sleep(2.3)
oldtime = (time.time())

#Define what happens when a key is pressed, 
#while making sure that at least 2 seconds have passed
def key_press(key):
    global curtime
    global oldtime
    curtime = (time.time())
    if (curtime - 2) >= oldtime:
        lm.on_for_rotations(25, rot)
        time.sleep(0.5)
        oldtime = time.time()

#Start waiting for a key to be pressed. The (key_press) part is what happens,
#see above for the key_press function
keyboard.on_press(key_press)

#Play a tune so that the user knows that the script is ready
sound.tone([(493.88, 500, 500), (440, 500, 500), (523.25, 500, 500)])

#Keep the program alive
while True:
    time.sleep(0.1)
