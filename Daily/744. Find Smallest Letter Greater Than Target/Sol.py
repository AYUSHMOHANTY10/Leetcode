class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        for i in l:
            s=0
            r=len(l)-1
            while s<=r:
                mid=(s+r)//2
                if l[mid]<=t:
                    s=mid+1
                else:
                    r=mid-1
        return l[s%len(l)]
                
