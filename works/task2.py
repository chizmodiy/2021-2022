def split_pairs(a):
    new_l = []
    new_r = []
    result = []
    string = f'{a}'
    if 0 < len(string) > 100:
        print('braak')
    else:
        print(string)
        if len(string) % 2 == 1:
            string = string + '_'
    x=len(string)/2
    x=int(x)
    print(string)
    counter = 0
    for i in string:
        counter += 1
        if counter % 2 == 1:
            new_l.append(i)
        else:
            new_r.append(i)
    print(new_l,new_r,x)
    if x%2==0:
        for _ in range(0, x):
            result.append(new_l[_] + new_r[_])
    else:
        for _ in range(0, x):
            result.append(new_l[_] + new_r[_])
    return result



if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")