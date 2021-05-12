# Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        ans = ''
        for i in bin(num)[2:]:
            if i == '1':
                ans += '0'
            else: 
                ans += '1'
                
        return int(ans, 2)
        
