# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        solution = root.val

        def traverseTree(node):
            nonlocal count, solution
            if node == None:
                return

            traverseTree(node.left)
            count +=1
            if count == k:
                solution = node.val
                return
            traverseTree(node.right)
            
        traverseTree(root)
        return solution
        