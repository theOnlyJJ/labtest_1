# Initialize a list of variables
variables = [2, 5, 8, 10]

# Define the condition for the while loop
index = 0
while index < len(variables) - 1:
    # Get the current pair of variables
    variable1 = variables[index]
    variable2 = variables[index + 1]

    # Perform addition, multiplication, division, and multiplication
    result_addition = variable1 + variable2
    result_multiplication = variable1 * variable2
    result_division = variable1 / variable2
    result_times = variable1 * variable2

    # Print the results
    print(
        f"Addition: {result_addition}, Multiplication: {result_multiplication}, Division: {result_division}, Times: {result_times}")

    # Move to the next pair of variables
    index += 2

# Print a message after the loop is finished
print("Loop finished.")