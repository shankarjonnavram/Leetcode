class Solution:
    def maxArea(self, height: List[int]) -> int:
        sz = len(height)
        maxm = -1
        lt = 0
        rt = sz-1
        while(lt<rt):
            minm = min(height[lt],height[rt])
            maxm = max(maxm,minm*(rt-lt))
            if(minm==height[lt]):
                lt+=1
            if(minm==height[rt]):
                rt-=1
        return maxm
        # for i in range(sz):
        #     for j in range(i+1,sz):
        #         minm = min(height[i],height[j])
        #         maxm = max(maxm,minm*(j-i))
        # return maxm
        