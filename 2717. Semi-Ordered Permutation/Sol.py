'''class Solution:
    def semiOrderedPermutation(self, l: List[int]) -> int:
        n=len(l)
        c=0
        if l[0]==1 and l[n-1]==n:
            return 0
        a=l.index(1)
        while a!=0:
            l[a],l[a-1]=l[a-1],l[a]
            a=a-1
            c=c+1
        b=l.index(max(l))
        while b!=n-1:
            l[b],l[b+1]=l[b+1],l[b]
            b+=1
            c+=1
        print(l)
        return c'''

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        idx1 = nums.index(1)
        idxn = nums.index(n)
        return (n - idxn - 1) + (idx1) - (idxn < idx1)
