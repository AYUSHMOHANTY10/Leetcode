2)
#27/05/2023
class Solution:
    def buyChoco(self, p: List[int], money: int) -> int:
        m=-1
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if p[i]+p[j]<=money:
                    m=max(m,money-(p[i]+p[j]))
                    print(m)
        if m==-1:
            return money
        return m
