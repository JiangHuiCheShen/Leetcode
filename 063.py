#063 不同路径 II
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # if obstacleGrid==[[1]]:
        #     return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[1 for i in range(n)] for i in range(m)]
        for i in range(m):              #上边界 如果遇到障碍物后面都是0
            if obstacleGrid[i][0] == 1:
                matrix[i][0] = 0
            else:
                matrix[i][0] = matrix[i - 1][0]
        for j in range(n):                 #左边界 如果遇到障碍物下面都是0
            if obstacleGrid[0][j] == 1:
                matrix[0][j] = 0
            else:
                matrix[0][j] = matrix[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:   #遇到障碍物为0
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]#等于左边和上边的和
        return matrix[m - 1][n - 1]