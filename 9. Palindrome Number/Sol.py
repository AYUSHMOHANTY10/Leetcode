'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        s=x[-1::-1]
        if s==x:
            return True
        return False
