# 30/10/2023
class Solution:
    def sortByBits(self, a: List[int]) -> List[int]:
        d=[]
        r=[]
        for i in a:
            b=bin(i)
            c=b.count("1")
            d.append([int(c),i])
        d.sort()
        print(d)
        for i in range(len(d)):
            r.append(d[i][1])
        return r
        
