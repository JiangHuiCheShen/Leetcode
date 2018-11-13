# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 94. 二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历。
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        """
        if root is None:
            return []

        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root, ans):
        if root:
            self.inorder(root.left, ans)
            ans.append(root.val)
            self.inorder(root.right, ans)

        return ans

