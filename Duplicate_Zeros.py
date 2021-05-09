'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i<len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i, 0)
                i += 1
            i += 1
                
