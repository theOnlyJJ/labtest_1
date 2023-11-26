import bmi

print("test_bmi")

def test_calculate_bmi_under():
    print("")
    assert (bmi.calculate_bmi(1.73, 42) == -1)

def test_calculate_bmi_normal():
    print("")
    assert (bmi.calculate_bmi(1.73, 57) == 0)

def test_calculate_bmi_over():
    print("")
    assert (bmi.calculate_bmi(1.73, 87) == 1)

