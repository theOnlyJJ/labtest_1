# Define a dictionary to store employee information
employee_data = {
    "John": {"age": 30, "department": "Sales", "salary": 50000},
    "Jane": {"age": 25, "department": "Marketing", "salary": 60000},
    "Mary": {"age": 23, "department": "Marketing", "salary": 56000},
    "Chloe": {"age": 35, "department": "Engineering", "salary": 70000},
    "Mike": {"age": 32, "department": "Engineering", "salary": 65000},
    "Peter": {"age": 40, "department": "Sales", "salary": 60000}
}

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = {name: info for name, info in employee_data.items() if age_lower_limit < info["age"] < age_upper_limit}
    return result

def calculate_average_salary():
    total_salary = sum(info["salary"] for info in employee_data.values())
    average_salary = round(total_salary / len(employee_data), 2)
    return average_salary

def get_employees_by_dept(department):
    result = {name: info for name, info in employee_data.items() if info["department"] == department}
    return result

def display_records(employee_info):
    print(("Name" + "\t" + "Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(15))
    for name, info in employee_info.items():
        print((name + "\t" + str(info["age"]) + "\t" + info["department"] + "\t" + str(info["salary"])).expandtabs(15))

def display_main_menu():
    print("\n----- Employee Information Tracker -----")
    print("Select option\n")
    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")
    print("Q - Quit")

    option = input("Enter selection => ")

    if option == '1':
        display_records(employee_data)
    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))
    elif option == '3':
        age_lower_limit = int(input("Age (Lower Limit) = "))
        age_upper_limit = int(input("Age (Upper Limit) = "))
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)
    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)
    elif option.upper() == 'Q':
        quit()

def main():
    while True:
        display_main_menu()

if __name__ == "__main__":
    main()
