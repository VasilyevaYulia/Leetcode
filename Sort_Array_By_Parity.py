#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#You may return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        b = []
        c = []
        for i in A:
            if i%2 == 0:
                b.append(i)
            else:
                c.append(i)
        return b + c
