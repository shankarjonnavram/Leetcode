class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lt = []
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            left, right  = i+1 ,len(nums) -1
            while(left<right):
                val = a+nums[left]+nums[right]
                if val>0:
                    right-=1
                elif val<0:
                    left+=1
                else:
                    lt.append([a,nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
            
        return lt

        