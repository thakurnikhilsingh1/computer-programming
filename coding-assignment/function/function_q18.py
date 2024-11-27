# Find the Second Largest Number in a List
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

print(second_largest([4, 1, 3, 2, 5]))  

