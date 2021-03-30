#Given an array of integers nums.
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#Return the number of good pairs.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        a = {}
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num == nums[j]:
                    ans += 1
        return ans
        
