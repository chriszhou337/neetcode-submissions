# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def treeHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            return 1 + max(treeHeight(root.left), treeHeight(root.right))

        leftHeight = treeHeight(root.left)
        rightHeight = treeHeight(root.right)

        currentDiameter = leftHeight + rightHeight

        return max(currentDiameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        