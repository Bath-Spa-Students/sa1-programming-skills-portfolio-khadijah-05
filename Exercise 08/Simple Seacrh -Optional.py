#Optional Requirements

#The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). 
list_of_the_name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] 

#Making a string for "Sam".
searching_for_a_name  = input("Enter the name you are searching for: ")

#Using if-else statement to search for "Sam".
if searching_for_a_name in list_of_the_name:
    print(f"{searching_for_a_name} found in the list.")
else:
    print(f"{searching_for_a_name} not found in the list.")
