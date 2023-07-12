class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sz= len(nums)
        lt = [1]*sz
        prefix = 1
        for i in range(sz):
            lt[i] = prefix
            prefix*=nums[i]
        postfix=1
        for i in range(sz-1,-1,-1):
            lt[i]=lt[i]*postfix
            postfix*=nums[i]
        return lt
            
        