class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in s:
            if i.isalnum()==False:
                s=s.replace(i,"")
        l=len(s)+1
        p=s[l::-1]
        print(s," 000 ",p)
        if s==p:
            return True
        else:
            return False
