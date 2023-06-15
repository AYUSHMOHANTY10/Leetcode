class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        arr=s.split()
        if len(p)!=len(arr):
            return False
        
        for i in range(len(arr)):
            if p.find(p[i]) != arr.index(arr[i]):
                return False
        return True

