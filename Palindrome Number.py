#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)[::-1]
        if str(z) == str(x):
            return True
        else:
            return False
