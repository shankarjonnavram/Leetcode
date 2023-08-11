class Solution:
    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        res = ""
        reslen = 0 
        left = -1
        right = -1
        for i in range(sz):
            # Odd Condition
            lt = i
            rt = i
            while(lt>=0 and rt<sz and s[lt]==s[rt]):
                if(rt-lt+1 > reslen):
                    # res = s[lt:rt+1]
                    left = lt
                    right = rt
                    reslen = rt-lt+1
                lt-=1
                rt+=1
            # Even Condition
            lt ,rt = i , i+1
            while(lt>=0 and rt<sz and s[lt]==s[rt]):
                if(rt-lt+1 > reslen):
                    # res = s[lt:rt+1]
                    left = lt
                    right = rt
                    reslen = rt-lt+1
                lt-=1
                rt+=1
        return s[left:right+1]
            
            
            
        