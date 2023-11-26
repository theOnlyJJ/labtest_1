import Lab3_Exercise2 as Lab3ex2

print("test_Lab3_Exercise2")
SORT_ASCENDING = 0
SORT_DESCENDING = 1


# REQ-01 Test sorting in ascending order
def test_Sort_Ascending():
    print("")
    result = []
    input_arr = [3, 2, 1, 6, 7, 4, 5]
    answer = [1, 2, 3, 4, 5, 6, 7]
    
    result = Lab3ex2.bubble_sort(input_arr, SORT_ASCENDING)
    assert (result == answer)


# REQ-02 Test sorting in ascending order
def test_Sort_Decending():
    print("")
    result = []
    input_arr = [3, 2, 1, 6, 7, 4, 5]
    answer = [7, 6, 5, 4, 3, 2, 1]
    
    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING)
    assert (result == answer)


# REQ-03 Test array with >= 10 elements
def test_Long_array():
    print("")
    input_arr = [3, 10, 2, 1, 8, 9, 6, 7, 4, 5]  # Contains 10 elements
    answer = 1

    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING)
    assert (result == answer)



# REQ-04 Test array with no element (i.e. empty array).
def test_Empty_array():
    print("")
    input_arr = []  # Contains no element
    answer = 0

    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING)
    assert (result == answer)



# REQ-05 Test array with non-integer element(s).
def test_Not_pure_integer_array():
    print("")
    input_arr = [3, 2, 1, 6, 7.7, 4, 5]  # Contains non-integer element
    answer = 2

    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING)
    assert (result == answer)


