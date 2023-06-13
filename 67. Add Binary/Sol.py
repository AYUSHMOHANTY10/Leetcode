class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m=0
        a=int(a,2)
        b=int(b,2)
        #a=int(bin(int(a)).replace("0b",""))
        #b=int(bin(int(b)).replace("0b",""))
        c=a+b
        c=bin(int(c)).replace("0b","")
        return c
