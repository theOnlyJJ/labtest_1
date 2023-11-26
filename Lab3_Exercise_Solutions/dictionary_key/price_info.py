
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

def total_cost_shopping():
    total_cost = 0
    '''
    Use the dictionary's keys() function to extract all the keys from the
    quantity_list dictionary (this is actually the "shopping list"). Then,
    for each key, check whether the key exists in the price_list dictionary.
    If it exists, get the per-unit price, multiply with the quantity to
    purchase to get the sub-total. Accumulating all the sub-total for
    every key in the quantity_list, the total shopping cost can be found.
    '''
    for key in quantity_list.keys(): # Extract all the keys from the quantity_list dictionary.
        if key in price_list: # If the key exists in the price_list dictionary.
            print(key + "\t", quantity_list[key],"x ", price_list[key], "= ", (price_list[key]*quantity_list[key]))
            total_cost = total_cost + (price_list[key]*quantity_list[key]) # Accumulate the sub-total
        else: # If the key does not exist in the price_list dictionary.
            print("Warning! The fruit '" + key + "' is not on the price list.")

    print("total cost = ", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    print("cost of ", quantity, fruit, "=", cost)
    return cost


# Below is an easier way to compute the cost of fruits.
def cost_of_fruits2(fruit, quantity):
    cost = price_list[fruit]*quantity
    print("cost of ", quantity, fruit, "=", cost)
    return cost
    

def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()


if __name__ == "__main__":
    main()
