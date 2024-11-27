# Generate a List of Squares
def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]

print(generate_squares(1, 5))
