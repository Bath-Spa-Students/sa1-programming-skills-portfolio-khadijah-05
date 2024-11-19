#For every item in a list, set etc. We make a set of statements once.
shopping_list = ["Bread", "Milk", "Eggs"]
for a in shopping_list:
  print(a)

#Activity  : Calculate square root of each number  in a range.   

#Defining the range.
for number in range (1,5):
  square_root = number ** 0.5
  print (square_root, "is the square root of ", number)

#Getting input from user. 
Number = int (input("Enter maximum number for range (1-100):"))
for b in range (0,100,2):
      print(b,end=",")
