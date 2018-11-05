class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #本质上和跳楼梯是一样的，跳一步还是两步，只不过要加一些限定条件
        dp=[0 for i in range(len(s)+1)]
        dp[0]=1
        for i in range(1,len(s)+1):
            if i>1 and (s[i-2]=='1' or(s[i-2]=='2' and s[i-1]<='6')): # 前两个数要在26范围内
                dp[i]+=dp[i-2]
            if s[i-1]!='0':
                dp[i]+=dp[i-1]
        return dp[-1]

a=Solution()
b=a.numDecodings('12')