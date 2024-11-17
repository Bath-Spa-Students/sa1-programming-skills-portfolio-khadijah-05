#Optional Requirement

#Defining the correct password.
password = "12345"

#Asking the user to enter the password.
asking_the_user_to_enter_the_password = " "

#Maximuming number of attempts.
maximum_number_of_attempts = 5
number_of_attempts_left = maximum_number_of_attempts

#Using a while loop to repeatedly ask the user for the password until the correct one is entered.
while asking_the_user_to_enter_the_password != password and number_of_attempts_left > 0 :
    asking_the_user_to_enter_the_password = input(f"You have {number_of_attempts_left} attempts. \nEnter the password:")
    
    #When the user enters the wrong password, informing them of the remaining attempts.
    number_of_attempts_left -=1

#Output an appropriate message when the correct password is entered.
if asking_the_user_to_enter_the_password == password:
    print("Permitted Access")
    
    #When the maximum number of attempts is reached, informing the user that the authorities have been alerted.
else:
    print("Maximum number of attempts is reached, the authorities have been alerted.")
    