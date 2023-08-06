class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sz = len(s)
        temp = 0
        st = ""
        out = ""
        for i in range(sz):
            temp+=1
            st+=s[i]
            if(temp==k*2):
                for j in range(k-1,-1,-1):
                    out+=st[j]
                for kt in range(k,k*2):
                    out+=st[kt]
                temp = 0
                st = ""
        if(temp<k*2 and temp>=k):
            for j in range(k-1,-1,-1):
                out+=st[j]
            # temp=temp-k
            for kt in range(k,temp):
                out+=st[kt]
        if(temp<k):
            for kt in range(temp-1,-1,-1):
                out+=st[kt]
        return out
                    
                
                
                
                
            
        
        