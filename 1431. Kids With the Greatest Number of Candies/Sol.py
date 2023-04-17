class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        a=max(candies)
        d=[]
        for i in candies:
            p=e+i
            if (p)>=a:
                d.append(True)
            else:
                d.append(False)
        return d
