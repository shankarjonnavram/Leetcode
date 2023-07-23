class Solution:
    def longestPalindrome(self, s: str) -> int:
        # dt = {}
        # for i in s:
        #     if(i in dt):
        #         dt[i]+=1
        #     else:
        #         dt[i]=1
        # s1 = 0
        # n1 = 0
        # for key in dt:
        #     if(n1==0 and dt[key]%2!=0):
        #         n1=(dt[key]//2)*2 + dt[key]%2
        #     else:
        #         s1+=dt[key]//2
        # return s1*2+n1
        
        st = set()
        # To get all characters which are present only once
        for i in s:
            if i not in st:
                st.add(i)
            else:
                st.remove(i)
        # Then checking the length of set.If Frequency is one we need to remove that count and add 1 (for odd length) .If len is 0 then everything is a palindrome
        if(len(st)!=0):
            return len(s)-len(st)+1
        else:
            return len(s)
