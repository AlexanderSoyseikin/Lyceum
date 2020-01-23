def are_friends(name, name1):
    return name1 in dict[name]


def print_friends(name):
    print(*sorted(dict[name]))


def add_friends(name, friend):
    if name in dict:
        dict[name] = dict[name] + friend
    else:
        dict[name] = friend


dict = {}
