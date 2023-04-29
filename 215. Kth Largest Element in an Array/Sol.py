class Solution:
    def findKthLargest(self, l: List[int], k: int) -> int:
        l.sort()
        a=len(l)
        return l[a-k]
