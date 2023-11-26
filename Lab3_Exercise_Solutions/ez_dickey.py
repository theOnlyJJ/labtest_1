# Price list for different fruits
price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95,
              'pomegranate': 4.95}

# Shopping list with quantities for each fruit
quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping():
    total_cost = sum(price_list.get(fruit, 0) * quantity for fruit, quantity in quantity_list.items())

    # Calculate and print the cost for each fruit in the shopping list
    for fruit, quantity in quantity_list.items():
        if fruit not in price_list:
            print("Warning! The fruit '" + fruit + "' is not on the price list.")
        else:
            print(f"{fruit}\t {quantity}x {price_list[fruit]} = {price_list[fruit] * quantity}")

    # Print the total cost of the shopping
    print("total cost =", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    # Calculate and print the cost of a specific fruit and quantity
    cost = price_list.get(fruit, 0) * quantity
    print(f"cost of {quantity} {fruit} = {cost}")
    return cost


def main():
    # Example: Calculate the cost of 10 apples
    cost_of_fruits('apple', 10)

    # Calculate the total cost of the shopping list
    total_cost_shopping()


if __name__ == "__main__":
    main()
