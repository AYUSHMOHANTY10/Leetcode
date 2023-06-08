'''class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        p=len(grid[0])
        for i in grid:
            l=0
            r=p-1
            while l<=r:
                mid=(l+r)//2
                if i[mid]<0:
                    r=mid-1
                else:
                    l=mid+1
            c+=p-l
        return c'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in grid:
            for j in i:
                if abs(j)!=j:
                    c=c+1
        return c
