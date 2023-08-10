class Solution:
    def reverseWords(self, s: str) -> str:
        st = ""
        lt = []
        for i in s:
            if i!=' ':
                st+=i
            else:
                if st:
                    lt.append(st)
                st = ""
        if st:
            lt.append(st)
        sz = len(lt)
        out = ""
        for i in range(sz-1,-1,-1):
            if(i==sz-1):
                out+=lt[i]
            else:
                out = out+" " + lt[i]
        return out