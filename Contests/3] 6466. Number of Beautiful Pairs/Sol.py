#25/6/23
class Solution:
    def countBeautifulPairs(self, nums):
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        def is_coprime(x, y):
            return gcd(int(x), int(y)) == 1
        
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if is_coprime(str(nums[i])[0], str(nums[j])[-1]):
                    count += 1
        
        return count
