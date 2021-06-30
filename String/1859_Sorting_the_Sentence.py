'''
Example:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
'''

class Solution:
    def sortSentence(self, s: str) -> str:
        
        '''
        ans = ''
        s = s.split()  #re.split(r'[ \s]', s)
        s = sorted(s, key=lambda x: int(x[-1]))
        for i in s:
            ans += i[:-1] + ' '
        return ans[:-1]
        '''
        
        d = {}
        for i in s.split():
            d[int(i[-1])] = i[:-1]
        ans = ""
        for i in range(1, len(s.split()) + 1):
            ans += d[i] + " "
            print(ans)
        return ans[:-1]
