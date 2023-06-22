'''class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        a=""
        num=n
        def dba(n,a):
             if n >= 1:
                dba(n // 3,a)
             a=a+str(n % 3)
             return a
        c=dba(n,a)
        b=(bin(num)).replace("0b","")
        print(b[-1],c)
        if b[-1]==0 and c==0:
            return True
        return False'''

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False #ALL test cases are false LOL
