# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def display_main_menu():
    print("Enter some numbers separated by commas (e.g 5,67,32)")


def calc_average():
    print("Average Calculation")


def get_user_input():
    user_input = input("Enter a sequence of numbers separated by commas: ")
    input_list = user_input.split(',')

    try:
        # Convert the list of strings to a list of floats
        float_list = [float(num) for num in input_list]
        return float_list
    except ValueError:
        print("Invalid input. Please enter a valid sequence of numbers separated by commas.")
        return get_user_input()

def check_input(input_string):
    return input_string == "_main_"


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    while True:
        display_main_menu()
        num_list = get_user_input()

        if check_input(num_list):
            print("You entered '_main_'. Goodbye!")
            break  # Exit the loop
        else:
            calc_average()


if __name__ == "__main__":
    main()