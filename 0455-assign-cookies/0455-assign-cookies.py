class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_sz = len(g)
        cookie_sz = len(s)
        ch = 0 
        cook = 0
        ct = 0
        # for i in range(child_sz):
        #     if(cook == cookie_sz):
        #         break
        #     while(cook<cookie_sz and s[cook]<g[i]):
        #         cook+=1
        #     if(cook<cookie_sz and s[cook]>=g[i]):
        #         ct+=1
        #         cook+=1
        while(ch<child_sz and cook<cookie_sz):
            if(s[cook]<g[ch]):
                cook+=1
            else:
                ct+=1
                cook+=1
                ch+=1
        return ct
    