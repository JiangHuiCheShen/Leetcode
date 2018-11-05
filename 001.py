# #1. 两数之和
# # 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# # 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。


#暴力法 两个循环
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for ii in range(len(nums) - i - 1):
            if nums[i] + nums[ii + i + 1] == target:
                return i, ii + i + 1


#哈希表 字典查询
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    newdict={nums[i]:i for i in range(len(nums))}

    newdict2 = {i: target-nums[i] for i in range(len(nums))}

    for i in range(len(nums)):
        Y=newdict.get((newdict2.get(i)))
        if Y is not None and (Y!=i):
            return i,Y
