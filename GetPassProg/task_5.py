def words_order(text: str, words: list) -> bool:
    text = text.split()
    if len(words) != len(text):
        while len(words) != len(text):
            words.append('_____')
    for id , value in enumerate(text):
        for id_2, value_2 in enumerate(words):
            if value == value_2:
                return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))
    assert words_order('hi world im here', ['here', 'world']) == False