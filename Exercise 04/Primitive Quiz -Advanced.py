#Advanced Requirements

#Extending the program into a quiz that asks for the capitals of 10 European countries.
#Storing the information in the dictionary.
question = {
    "What is the capital of France?": "Paris",
    "What is the capital of Germany?": "Berlin",
    "What is the capital of Italy?": "Rome",
    "What is the capital of Spain?": "Madrid",
    "What is the capital of United Kingdom?": "London",
    "What is the capital of Portugal?": "Lisbon",
    "What is the capital of Netherlands?": "Amsterdam",
    "What is the capital of Belgium?": "Brussels",
    "What is the capital of Sweden?": "Stockholm",
    "What is the capital of Norway?": "Oslo"
} 
for question, answer in question.items():
    
    #Using .strip() to accept answers regardless of the capitalization.
    user_answer = input(question + " " ).strip()
    if user_answer.lower() == answer.lower():

        #Checking if the user's answer is in correct, then printing correct.
        print("Correct")

        #If not correct, printing wrong.
    else:
        print ("Wrong")
