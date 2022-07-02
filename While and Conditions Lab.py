money = 50
shopping_cart = []
fruits = {"Apple": 5, "Banana": 10, "Raspberry": 20}

while True:
    if money <= 0:
        print("Thanks for shopping!")
        break
    else:
        player_choice = input(f"Select a fruit {fruits}:").title()
        if player_choice in fruits:
            if money >= fruits[player_choice]:
                shopping_cart.append(player_choice)
                money -= fruits[player_choice]
                print(f"Shopping cart: {shopping_cart} \nMoney left: {money}")
            else:
                print("You don't have enough money to make this purchase.")
        else:
            print("Invalid choice")