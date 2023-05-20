#Using loop
'''class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=list(s)
        while l[-1]==" ":
            l.pop()
        i=len(l)-1
        print(l,i)
        if i==0:
            return 1
        c=0
        while i>=0:
            if l[i]==" ":
                return c
            else:
                print(i,l[i],c,len(l))
                c=c+1
                i=i-1
        return c'''

#Using functions
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
