class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        ind = -1
        ''' 
        Finding Breaking point from the reverse of the array .
        Breaking point is the point where arr[i]<arr[i+1] from the reverse 
        Ex : For 2 1 5 4 3 0 0
        1 num is the breaking point .So , we need to store the index in ind               variable
        '''
        for i in range(sz-2,-1,-1):
            if(nums[i]<nums[i+1]):
                ind = i
                break
        '''
        If ind is -1 then the numbers are in decreasing order then we just need to         reverse the array
        '''
        if(ind==-1):
            for i in range(sz//2):
                nums[i] ,nums[sz-1-i] = nums[sz-1-i],nums[i] 
            return nums
        '''
        After finding the breaking point now we need to a number which is just             greater than that number and swap it with the breaking point number.
        As that next greater number will form the next permutation
        '''
        for i in range(sz-1,ind,-1):
            if(nums[i]>nums[ind]):
                nums[ind],nums[i]=nums[i],nums[ind]
                break
        '''
        Now we need to reverse all the digits from the number next to breaking             point to end of the array
        '''
        lt = ind+1
        rt = sz-1
        while (lt<rt):
            nums[lt],nums[rt] = nums[rt],nums[lt]
            lt+=1
            rt-=1
        return nums