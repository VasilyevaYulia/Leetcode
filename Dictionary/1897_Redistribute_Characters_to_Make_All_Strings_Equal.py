class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        d = {}
        joint = ''.join(words)
        
        for i in joint:
            if i not in d:
                d[i] = joint.count(i)
                
        for v in d.values() :
            if v % len(words) != 0 : return False 
        return True
