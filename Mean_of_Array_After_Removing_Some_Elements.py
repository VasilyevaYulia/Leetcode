#Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.
#Answers within 10-5 of the actual answer will be considered accepted.

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        section = int((len(arr))*5/100)
        interval = arr[section:len(arr)-section]
        mean = sum(interval)/len(interval)

        return mean
