class Solution:
    def longestPalindrome(self, s: str) -> int:
        dt = {}
        for i in s:
            if(i in dt):
                dt[i]+=1
            else:
                dt[i]=1
        s1 = 0
        n1 = 0
        for key in dt:
            if(n1==0 and dt[key]%2!=0):
                n1=(dt[key]//2)*2 + dt[key]%2
            else:
                s1+=dt[key]//2
        return s1*2+n1
            # print(f'key is {key} and value is {dt[key]}')