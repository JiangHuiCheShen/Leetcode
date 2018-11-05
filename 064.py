# #64. 最小路径和
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        mat = grid
        for i in range(1, m):  # 上边界
            mat[i][0] += mat[i - 1][0]

        for j in range(1, n):  # 左边界
            mat[0][j] += mat[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = min(mat[i - 1][j] + mat[i][j], mat[i][j - 1] + mat[i][j])
        return mat[-1][-1]