# Count the frequency of elements in a list using a dictionary
nums = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)

