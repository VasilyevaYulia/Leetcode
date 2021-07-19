#Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        ans = ''
        a = 0
        for i, j in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue=0):
            c = int(i)+int(j) + a
            if c < 10:
                ans += str(c)
                a = 0
            else:
                ans += str(c%10)
                a = c//10
        if a == 0:
            return ans[::-1]
        else:
            return (ans+str(a))[::-1]
