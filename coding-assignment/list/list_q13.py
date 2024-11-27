# Remove All Occurrences of an Element
def remove_element(lst, elem):
    return [x for x in lst if x != elem]

print(remove_element([1, 2, 3, 2, 4], 2))  
