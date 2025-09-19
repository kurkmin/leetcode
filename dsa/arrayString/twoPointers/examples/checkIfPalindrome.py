# Example 1: Given a string s, return true if it is a palindrome, false otherwise.
# A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. 
# For example: "abcdcba", or "racecar".

def check_if_palindrome(s):
    # use two pointers (left and right)
    left = 0
    right = len(s) - 1 
    while left < right: 
        if s[left] != s[right]: 
            return False 
        left += 1 
        right -= 1 
    return True 

# Test cases 

# palindrome 
s1 = 'abcdcba' 
s2 = 'racecar' 
# non-palindrome 
s3 = 'abcd' 

print(check_if_palindrome(s1))
print(check_if_palindrome(s2))
print(check_if_palindrome(s3))
