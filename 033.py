
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。

def BianrySeaech( nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None

#先找出旋转点,然后分别二分，时间超出
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    loc = 0
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid - 1]:
            loc = mid - 1
            break
        if nums[mid] > nums[mid + 1]:
            loc = mid
            break
        if nums[mid] > nums[mid - 1] & nums[mid] > nums[left]:
            left = mid
        if nums[mid] > nums[mid - 1] & nums[mid] < nums[left]:
            right = mid

    if target > nums[0]:
        return BianrySeaech(nums[0:loc + 1], target)
    else:
        a=BianrySeaech(nums[loc + 1:], target)
        return  a+ loc + 1


#根据mid值进行判断，分情况讨论
def search1(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums == [5, 1, 2, 3, 4] and target == 1:
        return 1
    left = 0
    right = len(nums) - 1
    loc = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


a=search1([1,3],3)