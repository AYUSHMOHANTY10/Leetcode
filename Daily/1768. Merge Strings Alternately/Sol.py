# 18/04/2023
class Solution:
    def mergeAlternately(self, m: str, n: str) -> str:
        a=len(m)
        b=len(n)
        x=""
        c=min(a,b)
        if a==c:
            for i in range(c):
                x=x+m[i]
                x=x+n[i]
            x=x+n[c::]
        else:
            for i in range(c):
                x=x+m[i]
                x=x+n[i]
            x=x+m[c::]
        return x
