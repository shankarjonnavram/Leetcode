class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        lt = []
        maxm =-1
        st =0
        for n,i in enumerate(s):
            while i in lt:
                lt.remove(lt[st])
            lt.append(i)
            maxm = max(maxm,len(lt))
            # if i not in lt:
            #     lt.append(i)
            # else:
            #     maxm=max(maxm,len(lt))
            #     while i in lt:
            #         lt.remove(lt[st])
            #     lt.append(i)
            #     maxm=max(maxm,len(lt))
        return maxm

                
                
        