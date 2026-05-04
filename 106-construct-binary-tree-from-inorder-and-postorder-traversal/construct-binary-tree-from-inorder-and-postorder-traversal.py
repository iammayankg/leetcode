# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        elemToPos = {elem: idx for idx, elem in enumerate(inorder)}
        
        def helper(left_in, right_in):
            if left_in > right_in:
                return None
            rootVal = postorder.pop()
            rootIdx = elemToPos[rootVal]
            root = TreeNode(rootVal)
            root.right=helper(rootIdx+1, right_in)
            root.left=helper(left_in, rootIdx-1)
            return root
        
        return helper(0, len(postorder)-1)