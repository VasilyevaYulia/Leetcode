'''
A string is good if there are no repeated characters.
Given a string s, return the number of good substrings of length three in s.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.
'''

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n-2):
            if len(set(s[i:i+3])) == 3:
                ans += 1 
        return ans
