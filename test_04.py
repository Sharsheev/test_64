def index_power(array, n):
    some_res = 0
    if some_res <= n < len(array):
        return array[n] ** n
    elif len(array) == 0:
        return -1

    print(some_res)
    return some_res

if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
