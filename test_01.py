import re


def second_word(text):
    some_result = re.findall(r'[a-zA-Z]+', text)[-1]
    return some_result


if __name__ == '__main__':
    print("Example:")
    # print(second_word("Hello world"))

    assert second_word("Hello world") == "world"
    assert second_word(" a word ") == "word"
    assert second_word("don't touch it") == "it"
    assert second_word("greetings, friends") == "friends"
    assert second_word("... and so on ...") == "on"
    assert second_word("hi") == "hi"
    assert second_word("Hello.World") == "World"
