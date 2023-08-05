class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if(len(nums)==0):
        #     return 0
        # nums.sort()
        # sz = len(nums)
        # maxm=1
        # ct=1
        # for i in range(1,sz):
        #     if(nums[i]!=nums[i-1] and nums[i]!=nums[i-1]+1):
        #         maxm = max(maxm,ct)
        #         ct=1
        #     else:
        #         if(nums[i]==nums[i-1]):
        #             continue
        #         else:
        #             ct+=1
        # return max(maxm,ct)
        
        #optimal 
        if(len(nums)==0):
             return 0
        st = set()
        maxm = 1
        for i in nums:
            st.add(i)
        for i in nums:
            if(i-1 in st):
                continue
            else:
                ct=1
                while(True):
                    i = i+1
                    if(i in st):
                        ct+=1
                    else:
                        maxm = max(maxm,ct)
                        break
        return maxm
                    
            
        