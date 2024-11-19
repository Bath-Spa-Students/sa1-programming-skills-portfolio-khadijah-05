#Advanced Requirements

#Extending the program into a quiz that asks for the capitals of 10 European countries.

#Storing the information in the dictionary.
storing_the_information = {
    "What is France's capital city?": "Paris",
    "What is Germany's capital city?": "Berlin",
    "What is Italy's capital city?": "Rome",
    "What is Spain's capital city?": "Madrid",
    "What is United Kingdom's capital city?": "London",
    "What is Portugal's capital city?": "Lisbon",
    "What is Netherland's capital city?": "Amsterdam",
    "What is Belgium's capital city?": "Brussels",
    "What is Sweden's capital city?": "Stockholm",
    "What is Norway's capital city?": "Oslo"
    } 
for storing_the_information, correct_answer in storing_the_information.items():
    
    #Using .strip() to consider the answer correct regardless of the spacing.
    user_input = input(storing_the_information + " " ).strip()

     #Using if-else statements.
    if user_input.lower() == correct_answer.lower():

        #Checking if the user's answer is in correct than printing correct.
        print("Correct Answer!")

     #If not correct than printing wrong.
    else:
        print ("Incorrect Answer!")