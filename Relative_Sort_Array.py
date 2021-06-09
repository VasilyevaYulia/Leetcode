#Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for i in arr1:
            if d.get(i) is None:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        output_1 = []
        for i in arr2:
            output_1 += [i]*d[i]
        output_2 = []
        for i in set(arr1)-set(arr2):
            output_2 += [i]*d[i]
        return output_1 + sorted(output_2)
