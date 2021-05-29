import re

def count_words(sentence):
    new_sentence = re.sub(r"\W+", ' ', sentence)
    new_sentence = new_sentence.lower()
    new_sentence = new_sentence.replace('_', ' ')
    words_list = new_sentence.split()
    words_count = {}

    for x in ["t", "s", "d"]:
        while x in words_list:
            i = words_list.index(x)
            words_list[i-1] = words_list[i-1] + "'" + words_list[i]
            words_list.remove(x)
    
    for item in words_list:
        counter = words_list.count(item)
        words_count.update({item: counter})
    return words_count

if __name__ == '__main__':
    x = "Joe can't tell between 'large' and large."
    y = "one,\ntwo,\nthree"
    z = "hey,my_spacebar_is_broken"
    print(count_words(x))
    print(count_words(y))
    print(count_words(z))
