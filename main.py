import tkinter as tk
import random

player = 1        # who's turn is it?  value should be either 1 or 2
p1_score = 0
p2_score = 0
turn_total = 0    # the number of points scored on the current turn

# This function should change who's turn it is.
# For example: If the current player is number 1, then make the
#   current player be number 2.
# Modify any other variables and GUI elements as needed.
def switch_players():
    global player, turn_total     # don't change this line
    pass


# Update the score Labels to have the current values
def update_scores():
    global p1_score, p2_score, turn_total   # don't change this line
    pass


# roll_value holds the die value that was rolled.  This method should
# update turn_total or change players as appropriate.  Call update_scores
# to change the displayed scores.
def do_turn(roll_value):
    global turn_total, player, p1_score, p2_score    # don't change this line
    pass


# This method is called when the 'Roll' button is clicked.
# roll_value will contain a random value from 1 through 6.
# Set the appropriate die image, then call do_turn.
def roll_clicked():
    roll_value = random.randint(1, 6)
    pass


# This function is called when the 'Hold' button is clicked.
# Display the Hold image and update scores and turns as appropriate.
def hold_clicked():
    global player, p1_score, p2_score, turn_total     # don't change this line
    pass


# Create your window and set the window title
window = tk.Tk()

# load all of the images into variables


# Create the GUI using Frames, Labels, and Buttons





window.mainloop()