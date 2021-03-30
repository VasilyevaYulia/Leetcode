'''
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.
'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['']*len(s)
        i = 0
        for j in enumerate(indices):
            ans[j[1]] = s[i]
            i += 1
        return ''.join(ans)
        
