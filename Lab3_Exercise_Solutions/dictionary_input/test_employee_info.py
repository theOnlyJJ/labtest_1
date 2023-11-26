import employee_info

print("test_employee_info")


def test_get_employees_by_age_range1():
    result = []
    answer = employee_info.employee_data[0:3]

    result = employee_info.get_employees_by_age_range(21, 31)
    assert (result == answer)


def test_get_employees_by_age_range2():
    result = []
    answer = [employee_info.employee_data[index] for index in [0,3,4]]

    result = employee_info.get_employees_by_age_range(29, 36)
    assert (result == answer)


def test_calculate_average_salary():
    answer = 60166.67

    result = employee_info.calculate_average_salary()
    assert (result == answer)

def test_get_employees_by_dept1():
    result = []
    answer = employee_info.employee_data[1:3]

    result = employee_info.get_employees_by_dept('Marketing')
    assert (result == answer)


def test_get_employees_by_dept2():
    result = []
    answer = [employee_info.employee_data[index] for index in [0, -1]]

    result = employee_info.get_employees_by_dept('Sales')
    assert (result == answer)
