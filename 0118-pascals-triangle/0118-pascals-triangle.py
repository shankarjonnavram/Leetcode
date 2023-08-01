class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        k =1
        while(k<numRows):
            temp_lt = []
            temp_lt.append(1)
            i = 0 
            while(len(temp_lt)<k):
                temp_lt.append(output[-1][i]+output[-1][i+1])
                i+=1
            temp_lt.append(1)
            output.append(temp_lt)
            k+=1
        return output
                
        