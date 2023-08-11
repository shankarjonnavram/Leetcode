class Solution:
    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        res = ""
        reslen = 0 
        for i in range(sz):
            # Odd Condition
            lt = i
            rt = i
            while(lt>=0 and rt<sz and s[lt]==s[rt]):
                if(rt-lt+1 > reslen):
                    res = s[lt:rt+1]
                    reslen = rt-lt+1
                lt-=1
                rt+=1
            # Even Condition
            lt ,rt = i , i+1
            while(lt>=0 and rt<sz and s[lt]==s[rt]):
                if(rt-lt+1 > reslen):
                    res = s[lt:rt+1]
                    reslen = rt-lt+1
                lt-=1
                rt+=1
        return res
            
            
            
        