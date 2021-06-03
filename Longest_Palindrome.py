# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = set()
        for i in s:
            if i not in a:
                a.add(i)
            else:
                a.remove(i)
        if len(a) != 0:
            return len(s) - len(a) + 1
        else:
            return len(s)
