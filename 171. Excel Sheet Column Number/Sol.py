class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        pos = 0
        for s in reversed(columnTitle):
        //64 IS THE ORD/ASCII VALUE OF 'A'
            ret += (ord(s) - 64) * pow(26, pos)
            pos += 1
        return ret
