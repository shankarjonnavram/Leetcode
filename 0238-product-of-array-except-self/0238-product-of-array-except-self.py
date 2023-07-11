class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lt = [1]
        sz= len(nums)
        for i in range(sz-1):
            lt.append(nums[i]*lt[len(lt)-1])
        rt=1
        for i in range(sz-1,-1,-1):
            lt[i]=lt[i]*rt
            rt*=nums[i]
        return lt
            
        