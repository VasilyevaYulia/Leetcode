class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        s1, s2, s3 = '', '', ''
        for i in firstWord:
            a = ord(i)-97
            s1 += str(a)
            
        for i in secondWord:
            a = ord(i)-97
            s2 += str(a)
            
        for i in targetWord:
            a = ord(i)-97
            s3 += str(a)
            
        return int(s1)+int(s2)== int(s3)
