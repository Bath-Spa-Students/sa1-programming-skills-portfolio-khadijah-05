#Exercise 6: Brute Force Attack 

#Defining the correct password.
password = "12345"

#Asking the user to enter the password.
asking_the_user_to_enter_the_password = " "

#Using a while loop to repeatedly ask the user for the password until the correct one is entered.
while asking_the_user_to_enter_the_password != password:
    asking_the_user_to_enter_the_password = input("Enter the password: ")

#Output an appropriate message when the correct password is entered.
print("Permitted Access")