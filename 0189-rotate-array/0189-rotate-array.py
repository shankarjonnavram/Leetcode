def reverse(lt,rt,nums):
    while(lt<rt):
        nums[lt],nums[rt]=nums[rt],nums[lt]
        lt,rt = lt+1 , rt-1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sz = len(nums)
        # lt = [1]*sz
        # for i in range(sz):
        #     lt[(i+k)%sz] = nums[i]
        # for i in range(sz):
        #     nums[i]=lt[i]
        sz = len(nums)
        k = k%sz        # lenght of k can be more than arr length .Then we only need to change those additional value. 
        reverse(0,len(nums)-1,nums) # reversing all elements in the list
        reverse(0,k-1,nums)         # reversing first k elements in the list
        reverse(k,len(nums)-1,nums) # reversing all elements after k in the list 
        
            