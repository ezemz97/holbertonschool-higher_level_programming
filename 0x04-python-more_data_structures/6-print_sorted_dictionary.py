def print_sorted_dictionary(a_dictionary):
    new = []
    for x, y in sorted(a_dictionary.items()):
        print ("{}: {}".format(x, y))
