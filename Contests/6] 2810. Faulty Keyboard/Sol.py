class Solution:
    def finalString(self, s: str) -> str:
        n=len(s)
        i=0
        while i!=n:
            if s[i]=="i":
                s=s[i-1::-1]+s[i+1:]
                n=n-1
                i=0
            i+=1
        return s
