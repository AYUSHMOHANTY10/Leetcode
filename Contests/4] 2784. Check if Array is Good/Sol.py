class Solution:
    def isGood(self, nums: List[int]) -> bool:
        a=max(nums)
        n=len(nums)-1
        if a==n and nums.count(a)==2:
            return True
        return  False
