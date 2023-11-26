
def calc_average_temperature(temperature_readings):
    if not temperature_readings:
        return 0.0  # Handle the case of an empty list to avoid division by zero
    return sum(temperature_readings) / len(temperature_readings)

def calc_median_temperature(temperature_readings):
    if not temperature_readings:
        return 0.0  # Handle the case of an empty list

    sorted_temperatures = sorted(temperature_readings)
    length = len(sorted_temperatures)

    if length % 2 == 1:
        # If the list has an odd number of elements, the median is the middle value.
        median = sorted_temperatures[length // 2]
    else:
        # If the list has an even number of elements, the median is the average of the two middle values.
        middle1 = sorted_temperatures[length // 2 - 1]
        middle2 = sorted_temperatures[length // 2]
        median = (middle1 + middle2) / 2

    return median

def calc_min_max_temperature(temperature_readings):
    if not temperature_readings:
        return [0, 0]  # Handle the case of an empty list
    min_temp = min(temperature_readings)
    max_temp = max(temperature_readings)
    return [min_temp, max_temp]
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
            average = calc_average_temperature(num_list)
            median = calc_median_temperature(num_list)
            min_max = calc_min_max_temperature(num_list)
            print(f"Average Temperature: {average:.2f}")
            print(f"Minimum Temperature: {min_max[0]}")
            print(f"Maximum Temperature: {min_max[1]}")
            print(f"Median Temperature: {median:.2f}\n")


if __name__ == "__main__":
    main()