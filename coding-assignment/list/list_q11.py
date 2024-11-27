# Find the Second Largest Element
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) > 1 else None

print(second_largest([4, 1, 2, 5, 3]))  
