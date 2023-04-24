class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        while len(s)!=1:
            a=max(s)
            s.remove(a)
            b=max(s)
            s.remove(b)
            if a!=b:
                x=abs(a-b)
                s.append(x)
            if a==b:
                s.append(0)
        if s[0]!=0:
            return s[0]
        return 0
