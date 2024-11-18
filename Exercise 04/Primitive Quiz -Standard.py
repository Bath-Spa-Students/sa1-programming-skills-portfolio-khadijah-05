#Exercise 4: Primitive Quiz

#Writing a program that asks the user "What is the capital of France?".
asking_the_user = input ("What is the capital of France?")

#If the answer is correct (i.e., "Paris"), printing a message saying the answer is correct.
if asking_the_user.lower() == "paris":
    print ("Correct Answer!")

#If the answer is incorrect, printing a message saying the answer is wrong.
else: 
    print("Incorrect Answer!")
