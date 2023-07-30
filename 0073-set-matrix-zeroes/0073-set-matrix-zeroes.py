class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row = []
        # col = []

        # for i in range(row_sz):
        #     for j in range(col_sz):
        #         if(matrix[i][j])==0:
        #             row.append(i)
        #             col.append(j)
        # for i in row:
        #     for j in range(col_sz):
        #         matrix[i][j] = 0
        
        # for i in col:
        #     for j in range(row_sz):
        #         matrix[j][i] = 0
        # return matrix
        row_sz = len(matrix)
        col_sz =  len(matrix[0])
        col0 = 1 
        '''
        Using first col and first row for storing the values which are empty. 
        As matrix[0][0] is common for both the list so we consider inbuilt one 
        for the row storing(which will be a col) and extra variable col0 
        where for the col storing row list will have only 3 items
        '''
        for i in range(row_sz):
            for j in range(col_sz):
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    if(j==0):
                        col0 = 0
                    else:
                        matrix[0][j]=0
        '''
        Here we iterate only the inner matrix leaving both the first row and col
        '''
        for i in range(1,row_sz):
            for j in range(1,col_sz):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
        '''
        
        '''
        if(matrix[0][0]==0):
            for j in range(col_sz):
                matrix[0][j]=0
        if(col0 ==0):
            for i in range(row_sz):
                matrix[i][0] =0 

        return matrix

        
        

            

