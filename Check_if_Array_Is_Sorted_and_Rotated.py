#Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
#There may be duplicates in the original array.

class Solution:
    def check(self, nums: List[int]) -> bool:
        s = sorted(nums)
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == s:
                return True  
        return False
