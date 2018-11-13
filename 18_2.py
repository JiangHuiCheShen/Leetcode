class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.backtracking(nums, target, 0, [], ans)

        return ans

    def backtracking(self, nums, target, value, temp, ans):
        if value == target and len(temp) == 4:
            ans.append(temp)
        else:
            if len(temp) < 4:
                for i in range(len(nums)):
                    self.backtracking(nums[i + 1:], target, value + nums[i], temp + [nums[i]], ans)
            else:
                return

test=Solution()
a=test.fourSum(nums=[1,0,-1,0,-2,2],target=0)