
def abbreviate(words):
    words = words.replace("-", " ")
    words = words.replace("_", " ")
    words_list = words.split()
    acronym = ""
    for word in words_list:
        acronym += word[0].upper()

    return acronym

if __name__ == '__main__':
    print(abbreviate('Good-mornning'))
    print(abbreviate('Good_mornning'))