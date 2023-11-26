# Using a for loop to iterate twice with two variables
for i in range(2):
    variable1 = float(input("Enter value for variable 1: "))
    variable2 = float(input("Enter value for variable 2: "))

    # Perform calculations
    result_multiply = variable1 * variable2
    result_divide = variable1 / variable2
    result_add = variable1 + variable2
    result_subtract = variable1 - variable2

    # Display results
    print(f"Iteration {i + 1}:")
    print(f"  Multiply: {result_multiply}")
    print(f"  Divide: {result_divide}")
    print(f"  Add: {result_add}")
    print(f"  Subtract: {result_subtract}")
    print()