#Advanced Requirement

#Making Adjustment for Leap Year.

#Defining a dictionary where the keys are month numbers and the values are the number of days in those months.
days_of_the_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

#Asking the user to input the month number.
month_number = int(input("Enter the month number(1-12):"))

#Using an if-else statement.
if 1 <= month_number <= 12:

    #Checking for February.
    if month_number  == 2:

        #Asking the user if the year is a leap year.
        for_leap_year = input ("It is a leap year? (yes/no):")

        #If the year is a leap year than printing the number of day in it.
        if for_leap_year == "yes":
            print(f"The number of days in 2 month is 29.")

         #If not a leap year than also printing the number of day in it.
        else:
            print(f"The number of days in 2 month is 28.")

         #If the input is valid than printing the number of days in the corresponding month.        
    else:
        print
 #For invalid month number, Asking the user to provide a valid month number.
else:
    print("Invalid month number, Please enter a number between 1 and 12.")
