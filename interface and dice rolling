# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:10:00 2018
@author: Jack
"""


#YIWEN ZHAO Start coding from here
import sys
sys.path.append("E:\PYLIB")
# import the appJar library
import random
from appJar import gui

def press(button):
    if button == "Exit":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
        if usr and pwd == "sjsu":
            print("You are now ready to play!")
        else:
            print("You are not Spartan.")
            

    if button == "Dice Rolling!":
        game_start = input("Would you like to roll the dice?")
        if game_start == 'yes':
            print("Your number is: " + str(random.randint(1,6)))
            
            play_again = input("Would you like to play again?")
           
            if play_again == 'yes':
                print("Your number is: " + str(random.randint(1,6)))
        else:
            print("No worries!You can still try our Sname game!")
            

    if button == "Snake Game!":
        app.stop()
        
#Kristie and Huy Start coding from here        
        """
        please enter snake codes here......
        """
        







































#Quan Gan Start coding from here
# create a GUI variable called app
app = gui("BUS92_SNAKE_TEAM!", "800x400")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to our games!")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)
app.addButton("Dice Rolling!",press)
app.addButton("Snake Game!",press)

app.setFocus("Username")

app.addButton("Exit",press)

# start the GUI
app.go()
