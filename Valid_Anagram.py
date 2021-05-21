#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        return sorted(s) == sorted(t)
        """
        mem = [0]*28
        empty = [0]*28
        for i in s:
            mem[ord(i)-97]+=1
        for i in t:
            mem[ord(i)-97]-=1
    
        
        return empty == mem
