class Solution(object):
    def search(self, nums, target):
        p=-1
        for i in range(len(nums)):
            if (nums[i]==target):
                p=i
                break
        return p
