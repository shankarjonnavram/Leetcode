class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt = []
        ind = -1
        maxm =-1
        st =0
        for n,i in enumerate(s):
            if i not in lt:
                lt.append(i)
                ind+=1
            else:
                maxm=max(maxm,len(lt))
                while i in lt:
                    lt.remove(lt[st])
                lt.append(i)
                maxm=max(maxm,len(lt))
                ind=len(lt)-1
        return max(maxm,len(lt))

                
                
        