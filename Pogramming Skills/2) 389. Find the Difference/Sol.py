class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i=0
        s=list(s)
        t=list(t)
        k=len(s)
        while k>0:
            if s[i] in t:
                t.remove(s[i])
                s.remove(s[i])
                k=k-1
            else:
                i=i+1 
        return t[0]  
