class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def helper(node, low, high):
            if not node:
                return 0
            if node.val < low:
                return helper(node.right, low, high)
            if node.val > high:
                return helper(node.left, low, high)
            return node.val + helper(node.left, low, high) + helper(node.right, low, high)

        return helper(root, low, high)
