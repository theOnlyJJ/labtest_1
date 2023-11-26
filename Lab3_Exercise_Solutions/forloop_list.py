# Initialize an empty list to store results
results = []

# Using a for loop to iterate twice with two variables
for i in range(2):
    variable1 = float(input("Enter value for variable 1: "))
    variable2 = float(input("Enter value for variable 2: "))

    # Perform calculations and store results in the list
    result_multiply = variable1 * variable2
    result_divide = variable1 / variable2
    result_add = variable1 + variable2
    result_subtract = variable1 - variable2

    # Append the results to the list
    results.append({
        "Multiply": result_multiply,
        "Divide": result_divide,
        "Add": result_add,
        "Subtract": result_subtract
    })

# Display the results
for i, result in enumerate(results, start=1):
    print(f"Iteration {i}:")
    for operation, value in result.items():
        print(f"  {operation}: {value}")
    print()