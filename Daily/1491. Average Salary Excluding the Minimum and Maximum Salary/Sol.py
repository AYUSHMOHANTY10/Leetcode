class Solution:
    def average(self, l: List[int]) -> float:
        l.sort()
        l.pop()
        l.pop(0)
        return sum(l)/len(l)
