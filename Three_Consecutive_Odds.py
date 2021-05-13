#Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0:
                return True
        return False
        
        """
        return "111" in "".join([str(i%2) for i in arr])
        """
