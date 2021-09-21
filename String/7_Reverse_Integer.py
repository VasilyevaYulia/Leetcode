class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        if x < 0:
            a = str(x)[::-1]
            s = '-' + a[:-1]
        if x > 0:
            s = str(x)[::-1]
        z = int(s)
        if z < -2147483648 or z > 2147483647:
            return 0
        return z
        
