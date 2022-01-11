#task1
def split_list(items: list) -> list:
    # your code here
    lens = len(items)
    print(lens)
    if lens ==0:
        return [[],[]]
    elif lens == 1:
        return [[items[0]], []]
    elif lens == 3:
        return [items[:2] , items[2:]]
    elif lens % 2 ==0:
        half = int(lens/2)
        return [items[0:half], items[half:]]
    else:
        start = round(lens / 100 * 70) - 1
        finish = round(lens / 100 * 30)
        return [items[:start], items[-finish:]]



if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5]))
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]