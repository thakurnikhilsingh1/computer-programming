#  Find the Index of an Element in a Tuple
def find_index(tup, elem):
    return tup.index(elem) if elem in tup else -1

print(find_index((1, 2, 3, 4), 3))
