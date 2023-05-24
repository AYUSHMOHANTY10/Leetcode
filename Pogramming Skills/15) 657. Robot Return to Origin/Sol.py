"""class Solution:
    def judgeCircle(self, moves: str) -> bool:
        R=1
        L=-1
        U=2
        D=-2
        c=0
        for i in moves:
            if ord(i)==82:
                c=c+1
            if ord(i)==76:
                c=c-1
            if ord(i)==85:
                c=c-10
            if ord(i)==68:
                c=c+10
        if c==0:
            return True
        return False"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:

        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
