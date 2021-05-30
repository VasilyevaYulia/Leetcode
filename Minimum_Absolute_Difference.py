#Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        target = min(m)
        ans = []
        for i,n in enumerate(m):
            if n == target:
                ans.append([arr[i],arr[i+1]])
        return ans
