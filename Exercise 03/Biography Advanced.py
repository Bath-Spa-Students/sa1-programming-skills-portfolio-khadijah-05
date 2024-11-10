#Advanced Requirements

#Asking the user input their name, hometown, and age.
name = input("Enter your full name: ")  #Ensuring multiple words can be entered for name.
hometown = input("Enter your hometown: ")

#Ensuring age is valid.
while True:
 age = input("Enter your age: ")
 if not age.isdigit():
   print ("Invalid, please enter a number for age.")
   
 else:
   age = int(age)
   break
