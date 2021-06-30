class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        ans = 0
        for i in s:
            if i == '(':
                c+=1
            if i == ')':
                c-=1
            if c > ans:
                ans = c
        return ans
        
