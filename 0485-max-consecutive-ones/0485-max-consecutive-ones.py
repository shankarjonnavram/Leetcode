class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0
        maxm = 0
        for i in nums:
            if i==0:
                maxm = max(maxm,ct)
                ct=0
            else:
                ct+=1
        return max(maxm,ct)
        