#Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = set(ransomNote)
        for i in r:
            if ransomNote.count(i) <= magazine.count(i):
                continue
            else:
                return False
        return True
        #return all(ransomNote.count(letter) <= magazine.count(letter) for letter in set(ransomNote))
