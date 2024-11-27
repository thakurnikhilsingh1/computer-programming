# Check if a String is Palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("level"))  
print(is_palindrome("hello")) 
