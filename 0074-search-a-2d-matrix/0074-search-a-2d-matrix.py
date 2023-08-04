class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(matrix[0][0]>target):
            return False
        lt_ind = 0 
        rt_ind = len(matrix[0])-1 
        exist = False
        rt = len(matrix)-1 
        while(target<matrix[rt][0]):
            rt-=1
        while(lt_ind<=rt_ind):
            mid = (rt_ind + lt_ind) // 2;
            if(matrix[rt][mid] == target):
                exist = True
                break 
            elif(matrix[rt][mid] > target):
                rt_ind = mid-1
            elif(matrix[rt][mid] < target):
                lt_ind = mid + 1
        return exist
            
                
            
        