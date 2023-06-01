'''class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c=1
        for i in nums:
            if i<0:
                c=c*-1
            if i==0:
                return 0
        return c'''

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        
        if product < 0:
            return -1
        
        elif product >0:
            return 1
        
        else:
            return 0
        
