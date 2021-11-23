def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    result = 0
    values.add(one)
    values=sorted(values)
    print( f'Start {values,one}')
    next_one= values.index(one)+1
    statr = values.index(one)
    prev_one =values.index(one)-1
    print(values)
    if values[values.index(one)]==values[-1]:
        return values[prev_one]
    if values[prev_one]==values[-1]:
        return  values[next_one]
    if values[values.index(one)]==values[-1]:
        return values[prev_one]
    if (one-values[prev_one])==(values[next_one]-one):
        result=values[prev_one]
    if  (one-values[prev_one])>(values[next_one]-one):
        result = values[next_one]
    else:
        result= values[prev_one]
    return  result



if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1

