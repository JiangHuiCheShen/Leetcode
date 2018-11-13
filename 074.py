搜索二维矩阵
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。


#先找对应哪一行，再二分搜索
#和右上角元素的进行比较，比它大就和下一行最后一个元素进行对比
def BinarySearch( nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return True
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix == [] or matrix == [[]]:
        return False
    i = 0
    while target > matrix[i][len(matrix[0]) - 1]:
        i += 1
        if i == len(matrix):
            return False
    return BinarySearch(matrix[i], target)

a=searchMatrix([[1],[3]],3)
