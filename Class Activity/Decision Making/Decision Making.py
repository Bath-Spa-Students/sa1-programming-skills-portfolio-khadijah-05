#Getting the amount you have spent.
amount_you_spent = float(input("Enter the amount you have spent: "))

#Discount based on amount spent.
if amount_you_spent > 1000:
    discount = 20
else: 
    discount = 0

#The total amount after the discount.    
total_amount_after_discount = amount_you_spent -(amount_you_spent * discount/100)

#Printing the total amount after the discount.
print (f"Your discount is {discount}%, which makes your total amount to be ${total_amount_after_discount}")