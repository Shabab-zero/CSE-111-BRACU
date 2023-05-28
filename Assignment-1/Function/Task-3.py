# Task-3

def FoodPanda(item, location = 'Mohakhali'):
    menu = {
        'BBQ Chicken Cheese Burger': 250,
        'Beef Burger': 170,
        'Naga Drums': 200
    }
    delivery_charge = 40 if location == 'Mohakhali' else 60
    tax = menu[item] * 0.08

    total_price = menu[item] + delivery_charge + tax
    print('Total price:', total_price)

FoodPanda('Beef Burger', 'Dhanmondi')
FoodPanda('Beef Burger')