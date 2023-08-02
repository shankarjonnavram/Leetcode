class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = 0
        sz = len(nums)
        maxm = nums[0]
        for i in range(sz):
            out+=nums[i]
            maxm = max(maxm,out)
            if(out<0):
                out = 0
        return maxm
                
            
        