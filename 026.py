# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        jishu = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[jishu] = nums[i]
                jishu += 1
        nums[jishu] = nums[-1]
        jishu += 1
        return jishu
