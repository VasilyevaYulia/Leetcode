#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        b = 0
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in reversed(s):
            if a[i]>=b:
                ans=ans+a[i]
            else:
                ans=ans-a[i]
            b=a[i]
        return ans
