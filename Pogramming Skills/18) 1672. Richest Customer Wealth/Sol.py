class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        c=0
        for i in a:
            c=max(c,sum(i))
        return c
