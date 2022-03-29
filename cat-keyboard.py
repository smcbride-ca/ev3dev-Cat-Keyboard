#!/usr/bin/env python3

#Import the needed modules.
#Time for getting the time and waiting, LargeMotor for motor control,
# Leds for the leds, Sound for audio, and keyboard for input.
from time import sleep
from time import time
from ev3dev2.motor import LargeMotor
from ev3dev2.sound import Sound
from keyboard import on_press

connected = False

#Set up commands
while connected == False :
    try :
        lm = LargeMotor()
        connected = True
    except :
        print("Please connect a large motor\n")
sound = Sound()


#BEEP and then get user input on the number of rotations the motor will do.
#The "Try" part trys to run that command
#The "except" part is what runs if there is an error
#The "finally" part is what happens after.
sound.beep()
try:
    print("Rotation: ")
    rot = int(input("\b"))
except:
    print("\rThere was an error. Please try again.\nRotation: ")
    rot = float(input("\b"))
finally:
    print("Rotation set successfully")

#Set time variables
curtime = (time())
sleep(2.3)
oldtime = (time())

#Define what happens when a key is pressed, 
#while making sure that at least 2 seconds have passed
def key_press(key):
    global curtime
    global oldtime
    curtime = (time())
    if (curtime - 2) >= oldtime:
        lm.on_for_rotations(25, rot)
        sleep(0.5)
        oldtime = time()

#Start waiting for a key to be pressed. The (key_press) part is what happens,
#see above for the key_press function
on_press(key_press)

#Play a tune so that the user knows that the script is ready
sound.tone([(493.88, 500, 500), (440, 500, 500), (523.25, 500, 500)])

#Keep the program alive
while True:
    pass