#  Flatten a Nested List
def flatten_list(nested_lst):
    return [item for sublist in nested_lst for item in sublist]

print(flatten_list([[1, 2], [3, 4], [5]]))  
