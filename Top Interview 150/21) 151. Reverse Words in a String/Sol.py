class Solution:
    def reverseWords(self, s: str) -> str:
        p=""
        s=s.split()
        l=s[-1::-1]
        for i in l:
            p=p+" "+i
        return p[1::]
