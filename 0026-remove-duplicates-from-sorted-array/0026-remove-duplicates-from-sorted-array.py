class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for i in nums:
        #     while(nums.count(i)>1):
        #         nums.remove(i)
        # print(nums)
        sz = len(nums)
        ct = 1
        for i in range(1,sz):
            if(nums[i]!=nums[i-1]):
                nums[ct] = nums[i]
                ct+=1
        while(ct<sz):
            nums.pop(sz-1)
            sz-=1
       
            