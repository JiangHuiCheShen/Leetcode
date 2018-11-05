class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        right = len(nums) - 1
        while right >= 1 and nums[right - 1] >= nums[right]:
            right -= 1

        if right == 0:
            nums = nums[::-1]

        index = right - 1
        minindex = right
        while right < len(nums):
            if nums[right] > nums[index] and nums[right] < nums[minindex]:
                minindex = right
            right += 1
        nums[index], nums[minindex] = nums[minindex], nums[index]
        b = sorted(nums[index + 1:])
        nums = nums[:index + 1] + b

s=Solution()
nums=[1,3,2]
s.nextPermutation(nums)