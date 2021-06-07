def is_pangram(sentence):
    new_sentence = sentence.lower()
    for i in range(97, 123):
        if chr(i) not in new_sentence:
            return False

    return True


if __name__ == '__main__':
    print(is_pangram('the 1 quick brown fox jumps over the 2 lazy dogs'))
    print(is_pangram('five boxing wizards jump quickly at it'))