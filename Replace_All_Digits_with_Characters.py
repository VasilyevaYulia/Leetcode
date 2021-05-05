#You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            if i%2 == 1:
                ans += chr(ord(s[i-1])+int(s[i]))
            else:
                ans += s[i] 
        return ans
