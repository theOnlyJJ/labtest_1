import price_info

print("test_price_info")


def test_total_cost_shopping():
    print("")
    answer = 46.75
    result = price_info.total_cost_shopping()
    assert (result == answer)


def test_cost_of_fruits():
    print("")
    answer = 12.0
    result = price_info.cost_of_fruits('apple', 10)
    assert (result == answer)
