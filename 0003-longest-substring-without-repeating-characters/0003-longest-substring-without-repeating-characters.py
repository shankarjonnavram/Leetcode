class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if(len(s)==0):
        #     return 0
        lt = set()
        maxm =0
        left = 0
        for n,i in enumerate(s):
            while i in lt:
                lt.remove(s[left])
                left+=1
            lt.add(i)
            maxm = max(maxm,n-left+1)
            # if i not in lt:
            #     lt.append(i)
            # else:
            #     maxm=max(maxm,len(lt))
            #     while i in lt:
            #         lt.remove(lt[st])
            #     lt.append(i)
            #     maxm=max(maxm,len(lt))
        return maxm

                
                
        