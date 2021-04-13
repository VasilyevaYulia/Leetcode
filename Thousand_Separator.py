#Given an integer n, add a dot (".") as the thousands separator and return it in string format.

class Solution:
    def thousandSeparator(self, n: int) -> str:
        b = ''
        n = str(n)[::-1]
        for i in range(len(n)):
            if i%3 == 0 and i>0:
                print (n[i])
                b = b + '.' + n[i]
            else: b = b + n[i]
        return ''.join(b)[::-1]
