1)
#15/04/2023
class Solution:
    def findColumnWidth(self, g: List[List[int]]) -> List[int]:
        w=[]
        q=[]
        o=len(g)
        for i in g:
            for j in i:
                w.append(j)
        t=len(w)+1
        h=1
        if o>1:
            h=t/o
            h=int(h)
        if len(g[0])==1:
            h=1
            o=1
        for y in range(h):
            e=w[y:t:h]
            c=[]
            for j in e:
                
                if j<0:
                    j=str(j)
                    p=list(j)
                    c.append(len(p))
                else:
                    j=str(j)
                    p=list(j)
                    c.append(len(p))
            q.append(max(c))
        if (len(g[0])!=1 and h==1):
            for i in range(len(g)+1):
                q.append(q[0])
        return q
