class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return 1
        nums_set = set(nums)
        for i in range(1, max(nums) + 2):
            if i not in nums_set:
                return i
