# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                result.append(root.val)
        
        result = []
        postorder(root)
        return result