#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([c**2 for c in nums])
        
        #squares=list(map(lambda c:pow(c,2),nums))
        #return sorted(squares)
