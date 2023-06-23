class Solution:
    def sortTheStudents(self, a: List[List[int]], k: int) -> List[List[int]]:
        a.sort(key=lambda x:x[k],reverse = True)
        return a

'''class Solution:
    def sortTheStudents(self, a: List[List[int]], k: int) -> List[List[int]]:
        l=len(a)-1
        for i in range(l):
            for j in range(l):
                if a[j][k]<a[j+1][k]:
                    a[j],a[j+1]=a[j+1],a[j]
        return a'''
