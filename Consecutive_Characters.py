#Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
#Return the power of the string.

class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        count = 1
        a = s[0]
        for i in range(1,len(s)):
            if s[i] == a:
                count += 1
            else:
                a = s[i]
                count = 1
            ans = max(ans, count)
        return ans
