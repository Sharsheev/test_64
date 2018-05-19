def mult_odd(array):
    some_result = 0
    fn = array[-1]
    for x in array:
        if x % 2 != 0:
            some_result = some_result + x
        elif len(array) == 0 and len(array) == 1:
            return 0
        result = some_result * fn
    print(result)
    return result

# mult_odd([0, 1, 2, 3, 4, 5])
if __name__ == '__main__':
    assert mult_odd([0, 1, 2, 3, 4, 5]) == 45, "(1+3+5)*5=45"
    assert mult_odd([1, 3, 5]) == 15, "(3)*5=15"
    assert mult_odd([6]) == 0, "Тизмекте бир эле элемент бар = 0"
    assert mult_odd([]) == 0, "Тизмек бош = 0"
