#Exercise 8: Simple Search 
#Writing a program that searches for a specific string within a list of strings. 

#The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). ,
list_of_the_name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] 

#Making a string for "Sam".
searching_for_a_name  = "Sam"

#Using if-else statement to search for "Sam".
if searching_for_a_name in list_of_the_name:
    print(f"{searching_for_a_name} found in the list.")
else:
    print(f"{searching_for_a_name} not found in the list.")
