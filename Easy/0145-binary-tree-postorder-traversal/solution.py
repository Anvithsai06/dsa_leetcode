# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        r=[]
        def preorder(root):
            if root is None:
                return
            preorder(root.left)
            preorder(root.right)
            r.append(root.val)
        preorder(root)
        return r
