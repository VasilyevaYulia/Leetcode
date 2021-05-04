#Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
#We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                if i == 0:
                    nums[i] = min(nums[i+1], nums[i])
                    break
                else:
                    if nums[i-1] <= nums[i+1]:
                        nums[i] = max(nums[i+1], nums[i-1])
                        break
                    else:
                        nums[i+1] = max(nums[i], nums[i-1])
                        break
        return nums == sorted(nums) 
