# 不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#回溯法 超时
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        right = 0
        down = 0
        ans = 0
        self.ans = 0
        self.backtracking(m, n, right, down, [])
        return self.ans

    def backtracking(self, m, n, right, down, temp):
        if right == m - 1 and down == n - 1:
            self.ans += 1
        else:
            if right <= m - 1 and down <= n - 1:
                if right < m - 1:
                    self.backtracking(m, n, right + 1, down, temp)
                if down < n - 1:
                    self.backtracking(m, n, right, down + 1, temp)
            else:
                return
        return

#动态规划
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix =[[1 for i in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]
        return matrix[m-1][n-1]