variable1 = 2
variable2 = 5

# Define the condition for the while loop
while variable1 < 10 and variable2 > 0:
    # Perform addition, multiplication, division, and multiplication
    result_addition = variable1 + variable2
    result_multiplication = variable1 * variable2
    result_division = variable1 / variable2
    result_times = variable1 * variable2

    # Print the results
    print(
        f"Addition: {result_addition}, Multiplication: {result_multiplication}, Division: {result_division}, Times: {result_times}")

    # Update the variables within the loop
    variable1 += 1
    variable2 -= 1

# Print a message after the loop is finished
print("Loop finished.")