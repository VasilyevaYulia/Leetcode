#Given a square matrix mat, return the sum of the matrix diagonals.
#Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a = 0
        s = len(mat)
        for i in range(s):
            a += mat[i][i] + mat[s-i-1][i]
        if s%2 == 0:
            return a
        return a - mat[s//2][s//2]
