#Advanced Requirements

#Asking the user input their name, hometown, and age.

#Ensuring multiple words can be entered for name.
first_name = input("Enter your first name: ") 
second_name =  input("Enter your second name: ")
hometown = input("Enter your hometown: ")

#Ensuring age is valid.
while True:
 age = input("Enter your age: ")
 if not age.isdigit():
   print ("Invalid, please enter age in digits.")
 else:
   age = int(age)
   storing_the_information = {

    #Using variables with appropriate data types for each piece of information.
    "name": first_name + " " + second_name,
    "hometown": hometown,
    "age": age
    }
   print(f"Name: {storing_the_information['name']}\nHometown: {storing_the_information['hometown']}\nAge: {storing_the_information['age']}")
   break