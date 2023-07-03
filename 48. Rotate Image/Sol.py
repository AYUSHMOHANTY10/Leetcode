class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        l=[]
        p=0
        a=[]
        k=len(m)-1
        while p!=len(m):
            l=[]
            for k in range(len(m)-1,-1,-1):
                l.append(m[k][p])
            p=p+1
            a.append(l)
        m[::]=a
        print(a)
        return a
        
