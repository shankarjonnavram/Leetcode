class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # output = [[1]]
        # k =1
        # # while(k<numRows):
        # #     temp_lt = []
        # #     temp_lt.append(1)
        # #     i = 0 
        # #     while(len(temp_lt)<k):
        # #         temp_lt.append(output[k-1][i]+output[k-1][i+1])
        # #         i+=1
        # #     temp_lt.append(1)
        # #     output.append(temp_lt)
        # #     k+=1
        output = [[1]]
        for i in range(1,numRows):
            # temp_lt = [1]*(i+1)
            temp_lt = [1]
            for j in range(1,i):
                temp_lt.append(output[i-1][j-1]+output[i-1][j])
            temp_lt.append(1)
            output.append(temp_lt)
        return output
                
        