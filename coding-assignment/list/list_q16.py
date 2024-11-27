# Split a List into Even and Odd Numbers
def split_even_odd(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens, odds

print(split_even_odd([1, 2, 3, 4, 5]))
