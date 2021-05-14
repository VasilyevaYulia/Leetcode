#Given a 2D integer array matrix, return the transpose of matrix.
#The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            rows = []
            for j in range(len(matrix)):
                rows.append(matrix[j][i])
            transpose.append(rows)      
        return transpose
    
        '''
        rows=len(matrix)
        cols=len(matrix[0])
        transpose=[[0]*rows for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transpose[j][i]=matrix[i][j]      
        return transpose
        '''
