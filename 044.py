class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        dp[0][0] = 1

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][0] = dp[i - 1][0]
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1] | dp[i - 1][j - 1]
        if dp[-1][-1] == 1:
            return True
        else:
            return False
a=Solution()
b=a.isMatch("","*")