#Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        maxC = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                maxC = max(c, maxC)
                c = 0
        return max(c, maxC)
        
         '''
        ans = ''
        for i in nums:
            ans = ans + str(i)
        l = ans.split('0')
        return len(max(l))
        
        '''
