class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lt = []
        ct=0
        for i in nums:
            if(i>=0):
                if(i==0):
                    lt.append(0)
                else:
                    while(i>abs(nums[ct-1])):
                        lt.append(abs(nums[ct-1])**2)
                        ct-=1
                    lt.append(i**2)
            else:
                ct+=1
        while(ct>0):
            lt.append(abs(nums[ct-1])**2)
            ct-=1
        return lt
        