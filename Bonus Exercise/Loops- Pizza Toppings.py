#Writing a loop that prompts the user to enter a series of pizza toppings. 
while True:
    topping_for_pizza = input("Topping for your pizza or type 'quit' to quit adding topping: ")

    #Until they enter a'quit' value. 
    if topping_for_pizza.lower() == 'quit':
        break
    
    #As they enter each topping, Printing a message saying you’ll add that topping to their pizza.
    print(f"Adding {topping_for_pizza} to your pizza.")