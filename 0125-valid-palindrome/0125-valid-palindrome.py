def st_reverse(i,lt,n):
    if(i>=n//2):
        return True
    return lt[i]==lt[n-i-1] and st_reverse(i+1,lt,n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st= ""
        for i in s:
            if (i.isalnum()):
                st=st+i.lower()
        return st_reverse(0,st,len(st))
        
        