'''
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
    For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.
An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_operations = 0
        max_elem = 0
        for cur_num in nums:
            if cur_num <= max_elem:
                n_operations += max_elem - cur_num + 1
                max_elem += 1
            else:
                max_elem = cur_num
        return n_operations
        '''
        count = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                count += nums[i] - nums[i+1] + 1
                nums[i+1] += nums[i] - nums[i+1] + 1
        return count
        '''
