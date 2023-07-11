class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        sz = len(nums)
        right = 0
        # while(first<sz and last<sz):
        #     if(nums[last]==0):
        #         last+=1
        #     elif(nums[last]!=0 and nums[first]==0):
        #         nums[first],nums[last] = nums[last],nums[first]
        #         last+=1
        #         first+=1
        #     else:
        #         first+=1
        #         last+=1

        # Initially we keep both the left and right pointers at infdex 0.When right index is zero we just increment if not swap it with left 
        while(right<sz):
            if(nums[right]!=0):
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1

            
                

        



