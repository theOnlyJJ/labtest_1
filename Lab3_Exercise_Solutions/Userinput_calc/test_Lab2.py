import Lab2


print("test_Lab2")
input_arr = [33, 22, 32, 35, 26, 28]


def test_calc_min_max_temperature():
    print("")
    answer = [22, 35]
    result = Lab2.find_min_max(input_arr)
    assert (result == answer)
            


def test_calc_average_temperature():
    print("")
    answer = 29.33333
    result = Lab2.calc_average(input_arr)
    result = round(result, 5)  # Need to set the decimal points of the result before comparison.
    assert (result == answer)



def test_calc_median_temperature():
    print("")
    answer = 30.00000
    result = Lab2.calc_median_temperature(input_arr)
    result = round(result, 5)  # Need to set the decimal points of the result before comparison.
    assert (result == answer)
