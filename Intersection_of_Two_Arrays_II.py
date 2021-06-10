#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Hashmap method
        d = {}
        ans = []
        for i in range(len(nums1)):
            if nums1[i] not in d:
                d[nums1[i]] = [1, 0]
            else:
                d[nums1[i]][0] += 1
        
        for j in range(len(nums2)):
            if nums2[j] in d:
                d[nums2[j]][1] += 1
                
        for i, v in d.items():
            if min(v) > 0:
                ans.extend([i]*min(v))
        
        return ans
        
        '''
        #Two pointer method
        nums1.sort()
        nums2.sort()
        ans = []
        one, two = 0, 0
        
        while one<len(nums1) and two<len(nums2):
            if nums1[one] < nums2[two]:
                one += 1
            elif nums2[two] < nums1[one]:
                two += 1
            else:
                ans.append(nums1[one])
                one += 1
                two += 1
        return ans
        
        
        a = set(nums1).intersection(set(nums2))
        ans = []
        for i in a:
            b = min(nums1.count(i), nums2.count(i))
            for j in range(b):
                ans.append(i)
        return ans
        '''
