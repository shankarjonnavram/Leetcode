class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        sz = len(nums)
        last = sz-1
        mid = 0
        while(mid<=last):
            if(nums[mid]==0):
                nums[mid],nums[first] = nums[first] , nums[mid]
                first+=1
                mid+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                nums[mid],nums[last]=nums[last],nums[mid]
                last-=1
        return nums
        