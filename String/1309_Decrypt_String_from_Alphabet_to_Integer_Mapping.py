'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        w = string.ascii_lowercase
        ans = ''
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                ans += w[int(s[i-2:i])-1]
                i -= 3
            else:
                ans += w[int(s[i])-1]
                i -= 1
        return ans[::-1]
