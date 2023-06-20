class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=bin(x)
        y=bin(y)
        x=list(x)
        y=list(y)
        x.pop(0)
        x.pop(0)
        y.pop(0)
        y.pop(0)
        m=[] 
        p=len(x)
        q=len(y)
        if p>q:
            c=p-q
            m=["0"]*c
            for i in range (q):
                m.append(y[i])
            y=m[::]
        #print(m)
        if p<q:
            c=q-p
            m=["0"]*c
            for i in range (p):
                m.append(x[i])
            x=m[::]
        #print(y,"x",m)
        v=0
        print(x,y)
        for i in range(len(x)):
            if y[i]!=x[i]:
                v=v+1
        return v
