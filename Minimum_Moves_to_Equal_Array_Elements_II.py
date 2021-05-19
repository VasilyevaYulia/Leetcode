#Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
#In one move, you can increment or decrement an element of the array by 1.

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans = 0
        m = sorted(nums)[len(nums)//2] #mediana
        for i in nums:
            ans += abs(m - i) 
        return ans
