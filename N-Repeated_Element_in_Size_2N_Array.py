#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#Return the element repeated N times.

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int: 
        for i in A:
            if A.count(i) == (len(A)/2):
                return i
