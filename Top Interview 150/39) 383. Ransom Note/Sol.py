class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        r=list(r)
        for i in m:
            if i in r:
                r.remove(i)
        if r:
            return False
        return True
