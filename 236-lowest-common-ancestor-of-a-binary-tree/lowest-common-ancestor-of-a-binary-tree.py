# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = root

        def recurse(node):
            if not node:
                return 0

            left = recurse(node.left)
            right = recurse(node.right)
            mid = node == p or node == q
            if left + mid + right > 1:
                self.ans = node
            return left or right or mid
        
        recurse(root)
        # print("Answwer", self.ans.vala)
        return self.ans
