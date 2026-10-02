import time

#THEACTUAL MENU
menu = {
    "Bread": "5$",
    "Fries": "2$",
    "Salad": "6$",
    "Soup": "12$",
    "Cheeseburger": "8$",
    "Pizza": "10$",
    "Sandwich": "4$",
    "Pasta": "7$",
    "Chocolate": "15$",
    "Drinks": "3$"
}
total_price = 0
#USERS BASKET
cart = [] 

print("--- 🎊Hello! Welcome to FastFoods!🎊 ---")
time.sleep(.4)
for food, price in menu.items():
    print(f"- {food}: {price} dollars")

while True:

    order = input("\n'Q' to exit || 'reset' to clear orders || 'cart' to view your cart||\n'done' for cashout!\n\nPlease order to your liking:\n>").strip()


    if order.lower() == "q": #lower to clean janky input of Q or q.
        print("Stopping...")
        break
    elif order.lower() == "reset":
        print("The cart has been reset")
        cart.clear()
        continue
    elif order == "cart":
        print(cart)
        continue
    elif order == "done":
        print(f"Calculating your bill for\n {cart}\n --------------------------------------------------------------------------------")
        for item in cart:       # NEW. for EVERYITEM in [LIST]:
            stringval = menu[item] #GET ALL THE VALUES of ITEMS in [LIST]
            cleanval = stringval.replace("$", "") #NEW. [STRINGVARIBLE remove a certain character in them for typecasting]
            formatval = int(cleanval)
            total_price = total_price + formatval #CUZ. It's a loop. 1 item at a time. (5$ item) = (total_price + 10)=total_price + x = ... = total
            finalval = total_price
        print(f"Total: {finalval}$. Head over to the reception! Thank you!") #ERROR: same as below. Each iteration runs through it. Hence all addition is shown 
        cart.clear()    #ERROR: Had it inside the for loop. Hence, it only calculated 1 val and dunked    
        break #ERROR: same as above, first iteration hits break and stops running back for other items


    

    if order == "":                                 #whitespace cleared
        print("❌You did not type anything! Retry")
        continue #Back to top
    elif order.isdigit():                           #digit cleared
        print("❌Digits are not in the menu! Retry")
        # all 3 edgecases covered.
        continue
   

    if order.capitalize() in menu:
        cart.append(order.capitalize())
        print(f"✅Added {order} to {cart}.")
    else: 
        print("❌This item is not in the menu!")
        continue

    
       
# MADE WITH LOVE!!!     
# Plan: to make 2 word key's with 1 word inputs to match later on
# Plan: to add another UI; "Menu" -> to display again