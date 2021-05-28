def is_isogram(string):
    item = 0
    while item < len(string):
        member = item + 1
        while member < len(string):
            if string[item] == string[member] or string[item] == string[member].swapcase():
                if string[item] not in [' ', '-']:
                    return False
            member += 1
        item += 1
    return True

