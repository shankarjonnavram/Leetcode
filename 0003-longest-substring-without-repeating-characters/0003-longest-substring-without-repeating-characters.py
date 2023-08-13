class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1):
            return 1
        # charset = set()
        # maxm =0
        # left = 0
        # for right, val in enumerate(s):
        # # Checking duplicate char in set .remove all the chars in order of string from set
        #     while val in charset:
        #         charset.remove(s[left])
        #         left+=1
        #     charset.add(val)
        #     maxm = max(maxm,right-left+1)
        # return maxm
        mp = {}
        left = 0
        maxm = 0
        for right,val in enumerate(s):
            if val in mp:
                left = max(mp[val]+1,left)
                mp[val] = right
            else:
                mp[val] = right
            maxm = max(maxm,right-left+1)
        return maxm

            # if i not in lt:
            #     lt.append(i)
            # else:
            #     maxm=max(maxm,len(lt))
            #     while i in lt:
            #         lt.remove(lt[st])
            #     lt.append(i)
            #     maxm=max(maxm,len(lt))


                
                
        