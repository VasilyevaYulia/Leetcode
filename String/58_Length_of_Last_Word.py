class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        while len(s) != 0:
            if s[-1] == ' ':
                s = s[: -1]
            else:
                return len(s.split(" ")[-1])
        return 0
