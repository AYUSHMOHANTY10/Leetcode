class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0 
        n = len(mat)
        for i in range(n):
            s += mat[i][i]
            s += mat[n-1-i][i] 
        if n % 2 != 0: s -= mat[n//2][n//2]
        return s

        
