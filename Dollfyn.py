## THIS WAS WRITTEN, COMPREHENDED BY, AND TESTED BY BUGZOOO
## plz dont steal code
## u can use as long as you note me
## thank u

import random
import time
import os
from datetime import datetime

## Serial number
## Im hoping to eventually be able to save users numbers and maybe call them back?
## I want to at least allow the code to learn on its own and keep track of new
## information through these numbers, or something like that.
serialnum = random.randint(1,1000000000000000)

## User input is saved just because.
uinput = ""

## "Loading" screen to make the program feel more interesting
def loading():
    print("loading")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    os.system('cls')

## This basically is called all the time to make sure the user isnt trying to leave
## i hate text based python "UI"s
## Before some angry chad comments about how I could have done this within the while loop instead of as a function
## I know that. I just hate them and I always find useless bugs involved with them so shut up.
def quit(uinput):
    if uinput == "quit":
        exit()
    elif uinput == "Quit":
        exit()
    elif uinput == "QUIT":
        exit()

## yes. i could have made it easily in the while loop. shut up im doing it my way. this is the same as the quit function.
## This is all basic quesstions one might ask an AI, like what its name is, saying thank you, etc.
def answer(uinput):
    uinput = input().lower()
    quit(uinput)
    if uinput == "what time is it":
        print(datetime.now())
    elif uinput == "what is your name":
        print("My name is Dolfyn. I was created as a small project in artificial intelligence.")
    elif uinput == "thanks":
        print("You are very welcome, I am programmed to help after all!")
    elif uinput == "thank you":
        print("You are very welcome, I am programmed to help after all!")
    else:
        print("I have no specification on ",uinput,)
    

loading()

## Greet screen. Basic. Bleh
print("Serial number:",serialnum)
print()
print("Welcome to Dolfyn, a generative artificial intelligence.")
print("What can I do for you today?")

## This is where the fun starts. And the pain. ;-;
while 1 == 1:
    answer(uinput)
