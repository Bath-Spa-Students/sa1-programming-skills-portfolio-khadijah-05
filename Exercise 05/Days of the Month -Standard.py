#Exercise 5: Days of the Month

#Defining a dictionary where the keys are month numbers and the values are the number of days in those months.
days_of_the_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
#Asking the user to input the month number.
month = int(input("Enter the month number(1-12):"))

#Using an if-else statement.
if 1 <= month <=12:
    #If the input is valid than printing the number of days in the corresponding month.
    print(f"The number of days in month {month} is {days_of_the_month[month]}.")
    
#For invalid month number, Asking the user to provide a valid month number.
else:
    print("Invalid month number, Please enter a number between 1 and 12.")
