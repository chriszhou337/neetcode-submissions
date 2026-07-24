# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        solution = []

        queue = deque([root])

        while len(queue) != 0:
            values = []
            n = len(queue)

            for i in range (0, n):
                values.append(queue[i].val)
            
            solution.append(values)

            for i in range (0, n):
                temp = queue.popleft()
                
                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

        
        return solution