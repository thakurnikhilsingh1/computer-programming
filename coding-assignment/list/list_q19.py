# Find the Difference Between Two Lists
def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

print(list_difference([1, 2, 3], [3, 4])) 
