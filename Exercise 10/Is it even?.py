#Exercise 10: Is it even? 

#Writing a program that tests if a value is even or odd. 

#The entered number is passed to a function that determines if the value is even or odd.
def checking_if_it_is_even_or_odd(number):
 
 #The function returns a message indicating whether the number is even or odd.
 if number %2 == 0:
  return "The entered number is even."
 else:
  return "The entered number is odd."

#Asking the user for a number from within the main function.
def main ():
  asking_the_for_the_input =  int(input ("Enter a number:"))
  result = checking_if_it_is_even_or_odd(asking_the_for_the_input)

  #The message returned by the function should be printed from within the main function.
  print(result)
  
main()