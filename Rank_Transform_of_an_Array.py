#Given an array of integers arr, replace each element with its rank.
#The rank represents how large the element is. The rank has the following rules:
#Rank is an integer starting from 1.
#The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
#Rank should be as small as possible.

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        d = {}
        k = 1
        sort = sorted(arr)
        for i in range(len(arr)):
            if sort[i] not in d:
                d[sort[i]] = k
                k += 1
                
        for i in arr:
            ans.append(d[i])
        return ans
