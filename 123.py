class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        left = []
        maxval = 0
        start = 0
        for i in range(len(prices)):
            if prices[i] < prices[start]:
                start = i
            left.append(max(prices[i] - prices[start], maxval))
        right = []
        maxval = 0
        start = len(prices) - 1
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > prices[start]:
                start = i
            right.append(max(prices[start]-prices[i], maxval))

        maxval = 0
        for i in range(len(prices)):
            maxval = max(maxval, left[i] + right[i])

        return maxval


a=Solution()
val=a.maxProfit([3,3,5,0,0,3,1,4])