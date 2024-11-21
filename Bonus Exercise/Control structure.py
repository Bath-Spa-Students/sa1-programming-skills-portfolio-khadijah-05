#Imagine an alien was just shot down in a game. 

#Creating a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color = 'red'

#Writing an if statement to test whether the alien’s color is green. If it is, printing a message that the player just earned 5 points.
if alien_color == "red":
    print ("You earned 5 point.")

#Writing a version of this program that passes the if test and another that fails. The version that fails will have no output.
alien_color = 'yellow'
if alien_color == "green":
    print ("You earned 5 point.")