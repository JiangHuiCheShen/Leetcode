def sortColors( nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    left = 0
    right = len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1  # left左边的都是0
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]  # right右边的都是2，交换完还要再判断nums[i]的情况，所以i不+1
            right -= 1
        elif nums[i] == 1:
            i += 1

sortColors([2,0,2,1,1,0])