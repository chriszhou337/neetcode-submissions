# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if (root and not subRoot) or (not root and subRoot):
            return False
        
        subTreeFound = False

        if root.val == subRoot.val:
            subTreeFound = self.isSameTree(root, subRoot)
        
        return subTreeFound or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p and not q) or (not p and q):
            return False

        nodesSame = p.val == q.val
        leftSame = self.isSameTree(p.left, q.left)
        rightSame = self.isSameTree(p.right, q.right)

        return nodesSame and leftSame and rightSame