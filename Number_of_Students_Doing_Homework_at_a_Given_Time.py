#Given two integer arrays startTime and endTime and given an integer queryTime.
#The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c = 0
        for i, j in zip(startTime, endTime):
            if i <= queryTime <= j:
                c += 1
        return c
