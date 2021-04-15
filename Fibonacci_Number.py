#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return n
        a, b, c = 0, 1, 0
        while n > 1:
            n -= 1
            c = a + b
            a = b
            b = c
            print (c)
        return c
       # recursive solution
       # return self.fib(n-1) + self.fib(n-2)
