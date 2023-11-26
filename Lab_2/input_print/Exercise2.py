def display_main_menu():
    print("Main Menu")


def calc_average():
    print("Average Calculation")


def get_user_input():
    try:
        user_input = float(input("Enter a number or '_main_' to exit: "))
        return user_input
    except ValueError:
        print("Invalid input. Please enter a valid number.")
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