class Solution:
    def calPoints(self, o: List[str]) -> int:
        l=[]
        for i in o:
            if i.isdigit()==True:
                l.append(int(i))
            if len(i)>=2 and i[0]=="-":
                l.append(int(i))
            if i=="C":
                if len(l)!=0:
                    l.pop()
            if i=="D":
                if len(l)!=0:
                    l.append(l[-1]*2)
            if i=="+":
                if len(l)>1:
                    l.append(l[-1]+l[-2])
        return sum(l)
