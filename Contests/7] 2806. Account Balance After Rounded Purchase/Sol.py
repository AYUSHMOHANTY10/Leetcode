class Solution:
    def accountBalanceAfterPurchase(self, p: int) -> int:
        if p==100:
            return 0
        if p<10 and p>5:
            return 90
        if p<10 and p<5:
            return 100
        if p==5:
            return 90
        p=str(p)            
        if p[-1]=="5":
            c=int(p[-2]+p[-1])+5
            return 100-c
        if p[-1]>"5":
            c=(int(p[-2])+1)*10
            return 100-c
        if p[-1]<"5":
            c=int(p[-2]+"0")
            return 100-c
        if p[-1]=="0":
            return 100-int(p)
