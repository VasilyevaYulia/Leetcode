class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ans = []
        for i in words:
            c = ''
            for j in i:
                c += m[ord(j)-97]
            if c not in ans:
                ans.append(c)
        return len(ans)
