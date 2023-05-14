class Solution:
    def strStr(self, h: str, n: str) -> int:
        a=len(h)
        b=len(n)
        if n not in h:
            return -1
        for i in range(a):
            if h[i:i+b:]==n:
                return i
