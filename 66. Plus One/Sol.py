class Solution:
    def plusOne(self, s: List[int]) -> List[int]:
        l=""
        a=[]
        for i in s:
            l=l+str(i)
        p=int(l)
        p=p+1
        p=str(p)
        for i in p:
            a.append(int(i))
        return a
