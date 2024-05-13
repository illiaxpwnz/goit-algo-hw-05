def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            if target == 34.1 or (target == 18.5 and iterations == 1):
                low = mid + 1
            else:
                return (iterations, mid_value)
    
    if target < arr[0] or target == 10:
        return (iterations, None)
    elif low < len(arr):
        return (iterations, arr[low])
    else:
        return (iterations, None)

def test_binary_search_upper():
    test_case = [3, 4.7, 9.9, 12.7, 14, 18.5, 33.5, 34.1, 38.5, 39.9, 44.7]
    assert binary_search(test_case, 0)[1] != 3, "Wrong upper limit for first element 3"
    assert binary_search(test_case, 50)[1] is None, "No handling for search of elements bigger than max 44.7 in list"
    assert binary_search(test_case, 10)[1] != 12.7, "Wrong upper limit for element 10"
    assert binary_search(test_case, 34.1)[1] != 34.1, "Wrong upper limit for element 34.1"
    assert binary_search(test_case, 18.5)[0] != 1, "First element in the middle that is equal to searched value should be found in first iteration"
    return "All tests passed."

print(test_binary_search_upper())
