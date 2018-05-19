def check(number):
    convert_to_str = str(number)
    some_res = 1
    for x in convert_to_str:
        if x == '0':
            continue
        convert_to_int = int(x)
        some_res = some_res * convert_to_int
    return some_res

if __name__ == '__main__':
    assert check(4321) == 24
    assert check(98765) == 15120
    assert check(1001) == 1
    assert check(2018) == 16
    print('done')
