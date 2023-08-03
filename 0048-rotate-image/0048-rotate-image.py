class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        # First find the transpose of the matrix(rows to cols and cols to rows)  then reverse each row .

        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if(j>i):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(rows):
            matrix[i].reverse()
        return matrix
        