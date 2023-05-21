class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=[]
        m=[]
        n[::]=nums[::]
        m[::]=nums[::]
        n.sort()
        m.sort(reverse=True)
        if nums==n or nums==m:
            return True
        return False
