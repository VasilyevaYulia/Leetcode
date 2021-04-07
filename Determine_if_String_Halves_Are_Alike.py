#You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
#Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
#Return true if a and b are alike. Otherwise, return false.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s) + 1 
        a = s[0:l//2]
        b = s[l//2:]
        c1 = 0
        c2 = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i in a:
            if i in vowels:
                c1 += 1
        for i in b:
            if i in vowels:
                c2 += 1
        if c1 == c2:
            return True
        else: return False
