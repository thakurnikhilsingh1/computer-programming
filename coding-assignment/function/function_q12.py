# Check Armstrong Number
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)

print(is_armstrong(153))  
print(is_armstrong(123))  

