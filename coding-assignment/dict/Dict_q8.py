# Find keys with the highest value
scores = {'Alice': 90, 'Bob': 95, 'Charlie': 85}
max_value = max(scores.values())
top_scorers = [key for key, value in scores.items() if value == max_value]
print(top_scorers)

