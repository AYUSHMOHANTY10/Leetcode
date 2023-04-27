class Solution:
    def romanToInt(self, s: str) -> int:
        l=[1,5,10,50,100,500,1000]
        p=["I","V","X","L","C","D","M"]
        c=0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in s:
            for j in range(len(l)):
                if i==p[j]:
                    c=c+l[j]
        return c
