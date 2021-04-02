#Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#Given a balanced string s, split it in the maximum amount of balanced strings.
#Return the maximum amount of split balanced strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0 
        R = 0
        L = 0
        for i in s:
            if i == 'R':
                R += 1
            else:
                L += 1
            if R == L:
                ans += 1     
        return ans
