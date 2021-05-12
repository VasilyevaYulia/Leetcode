# Given an array of integers nums, you start with an initial positive value startValue.
#In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#Return the minimum positive value of startValue such that the step by step sum is never less than 1.

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        tmp = 0
        a = []
        for i in nums:
            tmp += i
            a.append(tmp)
        value = -min(a)+1
        if value < 1:
            return 1
        else: 
            return value
        
        '''
        a = list(accumulate(nums))
        print(a)
        if min(a) >0:
            return 1
        else:
            return(abs(min(a) - 1))
        '''
