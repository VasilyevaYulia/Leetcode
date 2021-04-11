#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        a = re.split('[\s]', s)
        b = ''
        for i in a:
            b += i[::-1] + ' '
        return b[:-1]
        #return " ".join(list(i[::-1] for i in s.split()))
