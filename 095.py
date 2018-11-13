# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 根据二叉查找树的构成性质：当选择i为根结点时，【1,2，···i-1】构成其左子树，【i+1,i+2,···，n】构成其右子树。

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = list(range(1, n + 1))
        ans = []

        return self.Trees(nums)

    def Trees(self, nums):
        ans = []
        if nums == []:
            return [None]
        # elif len(nums)==1:
        #     return [TreeNode(nums[0])]
        else:
            for i in range(len(nums)):

                left = self.Trees(nums[:i])
                right = self.Trees(nums[i + 1:])

                for i in range(len(left)):
                    for j in range(len(right)):
                        root = TreeNode(nums[i])
                        root.left = left[i]
                        root.right = right[j]
                        ans.append(root)
            return ans


sol=Solution()
sol.generateTrees(3)