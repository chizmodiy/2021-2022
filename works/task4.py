def backward_string_by_word(text: str) -> str:
    return ' '.join([ i[::-1] for  i in text.split(' ')])


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('world'))
    print(backward_string_by_word('hello world'))
    print(backward_string_by_word('hello   world'))
    print(backward_string_by_word('welcome to a game'))
