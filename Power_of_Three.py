#Given an integer n, return true if it is a power of three. Otherwise, return false.
#An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        return round(log(n, 3),9) == round(log(n, 3))
