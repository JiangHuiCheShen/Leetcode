class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dp=[[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        # for i in range(len(t)+1):
        #     dp[0][i]=1
        # exsit=True
        # for i in range(1,len(s)+1):
        #     if exsit:                        #
        #         exsit=False
        #         for j in range(i,len(t)+1):
        #             if s[i-1]==t[j-1] and dp[i-1][j-1]:
        #                 dp[i][j]=1
        #                 exsit=True
        #             else:
        #                 dp[i][j]=dp[i][j-1]
        #     else:
        #         return False
        # if dp[-1][-1]==1:
        #     return True
        # else:
        #     return False
        if len(t) < len(s):
            return False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            while s[i] != t[j]:
                j += 1
                if j == len(t):
                    return False

            i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False

s=Solution()
b=s.isSubsequence("abc","ahbgdc")