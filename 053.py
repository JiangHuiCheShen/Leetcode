class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen=nums[0]
        for i in range(len(nums)):
            for j in range(len(nums)-i):
                maxlen=max(maxlen,sum(nums[i:i+j+1]))
        return maxlen

