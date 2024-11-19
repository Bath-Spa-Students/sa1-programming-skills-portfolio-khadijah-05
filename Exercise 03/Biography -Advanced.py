#Advanced Requirements

#Asking the user input their name, hometown, and age.

#Ensuring multiple words can be entered for name.
name = input("Enter your full name: ")  
hometown = input("Enter your hometown: ")

#Ensuring age is valid.
while True:
 age = input("Enter your age: ")
 if not age.isdigit():
   print ("Invalid, please enter age in digits.")
 else:
   age = int(age)
   break