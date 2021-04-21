#You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
#Return the sum of all the unique elements of nums.

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if nums.count(i) == 1:
                ans.append(i)
        return sum(ans)
