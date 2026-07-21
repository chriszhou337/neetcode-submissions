# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # current node is target
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left

            current = root.right
            
            while current.left:
                current = current.left
            root.val = current.val
            root.right = self.deleteNode(root.right, root.val)


        return root