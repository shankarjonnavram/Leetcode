class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sz = len(nums)
        lt = [1]*sz
        for i in range(sz):
            lt[(i+k)%sz] = nums[i]
        for i in range(sz):
            nums[i]=lt[i]
            