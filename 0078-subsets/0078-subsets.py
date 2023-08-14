def sums(left,lt,arr,right,out):
    if(left==right):
        out.append(list(lt))
        return
    lt.append(arr[left])
    sums(left+1,lt,arr,right,out)
    lt.pop()
    sums(left+1,lt,arr,right,out)
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lt = []
        left = 0
        right = len(nums)
        out = []
        sums(left,lt,nums,right,out)
        return out
        