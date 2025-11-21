# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, currSum, curr, results):
            if not node:
                return
            

            currSum = currSum + node.val
            
            curr.append(node.val)
            if targetSum == currSum and node.left is None and node.right is None:
                results.append(curr[:])
            else:
                if node.left:
                    dfs(node.left, currSum, curr, results)
                if node.right:
                    dfs(node.right, currSum, curr, results)
            curr.pop()
        res = []
        dfs(root, 0, [], res)
        return res
        