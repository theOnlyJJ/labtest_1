print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    n = len(arr)

    if n == 0:  # REQ-04
        print("Empty array!")
        return 0

    if not all(isinstance(value, int) for value in arr):  # REQ-05
        print("Array contains non-integer element(s).")
        return 2

    if n >= 10:  # REQ-03
        print("Array has", n, "elements (max allowed is 9)!")
        return 1

    # Copy input list to results list
    arr_result = arr.copy()

    # Sorting logic
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (sorting_order == SORT_ASCENDING and arr_result[j] > arr_result[j + 1]) or \
               (sorting_order == SORT_DESCENDING and arr_result[j] < arr_result[j + 1]):
                arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    return arr_result


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order:")
    print("Return =", result)

    # Sort in descending order
    print("\nSorted array in descending order:")
    result = bubble_sort(arr, SORT_DESCENDING)
    print("Return =", result)

    # Try to sort an empty array
    arr_empty = []
    print("\nTry to sort an empty array:")
    result = bubble_sort(arr_empty, SORT_DESCENDING)
    print("Return =", result)

    # Try to sort an array with equal or more than 10 elements.
    arr_long = [64, 34, 25, 12, 22, 11, 90, 66, 34, 19, 10]
    print("\nTry to sort an array with equal or more than 10 elements:")
    result = bubble_sort(arr_long, SORT_DESCENDING)
    print("Return =", result)

    # Try to sort an array with non-integer elements.
    arr_mix = [64, 34, 25, 12.3, 22, 11, 90]
    print("\nTry to sort an array with non-integer elements:")
    result = bubble_sort(arr_mix, SORT_DESCENDING)
    print("Return =", result)


if __name__ == "__main__":
    main()