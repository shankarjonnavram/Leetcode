def sums(left,lt,arr,right,out):
    if(left==right):
        if lt not in out:
            out.append(list(lt))
        return
    lt.append(arr[left])
    sums(left+1,lt,arr,right,out)
    lt.pop()
    sums(left+1,lt,arr,right,out)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lt = []
        left = 0
        right = len(nums)
        out = []
        nums.sort()
        sums(left,lt,nums,right,out)
        return out
        