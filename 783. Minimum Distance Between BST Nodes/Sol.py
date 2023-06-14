# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        a=[]
        c=999999999999999999999999999999999999999999999999999999999
        def printInorder(root):
            if root:
                printInorder(root.left)
                a.append(root.val)
                printInorder(root.right)
        printInorder(root)
        print(a)
        while a:
            q=a.pop()
            for i in a:
                c=min(c,abs(q-i))
        return c
