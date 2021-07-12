'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] != t[i]:
                return False
            elif s[i] not in d and t[i] in d.values():
                return False
            else: d[s[i]] = t[i]
        return True
