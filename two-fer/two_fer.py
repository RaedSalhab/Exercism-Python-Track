def two_fer(*args):
    if len(args) == 0:
        return "One for you, one for me."

    else:
        return "One for " + args[0] + ", one for me."

def two_fer2(name = 'you'):
    return "One for " + name + ", one for me."


print(two_fer2('raed'))
print(two_fer2())
