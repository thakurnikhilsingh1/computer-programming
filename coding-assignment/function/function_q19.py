# Check Perfect Number
def is_perfect(num):
    return num == sum(i for i in range(1, num) if num % i == 0)

print(is_perfect(6))  
print(is_perfect(10)) 
