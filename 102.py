# 102. 二叉树的层次遍历

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        stack = []
        stack.append(root)
        ans = []
        temp = []
        current_level_num = 1  # 初始化一层的节点
        next_level_num = 0
        while stack:
            current = stack.pop(0)  # 每次出队列这一层都要计数-1
            current_level_num -= 1
            temp.append(current.val)
            if root.left != None:
                stack.append(current.left)
                next_level_num += 1  # 每次进队列这一层都要计数+1
            if root.right != None:
                stack.append(current.right)
                next_level_num += 1

            if current_level_num == 0:  # 一层处理完
                current_level_num = next_level_num
                next_level_num = 0
                ans.append(temp)
                temp = []
                current_level_num = 1
        return ans
