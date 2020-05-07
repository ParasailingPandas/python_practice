# Write a function that given a number as a string returns True 
# if it is a Palindrome and returns False if not a Palindrome

# Examples:
# - isPalindrome("121") returns True
# - isPalindrome("001") returns False
# - isPalindrome("2") returns True


def isPalindrome(num):
    num = str(num)
    if num[::-1] == num:
        return True 
    else:
        return False 

print(isPalindrome("121"))
print(isPalindrome("001"))
print(isPalindrome("2"))
print(isPalindrome(121))
