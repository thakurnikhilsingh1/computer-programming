# Find the Index of an Element
def find_index(lst, elem):
    return lst.index(elem) if elem in lst else -1

print(find_index([1, 2, 3], 2)) 

