class Solution(object):
    def isAnagram(self, s, t):
        s=list(s)
        t=list(t)
        t.sort()
        s.sort()
        if s==t:
            return True
        else:
            return False
