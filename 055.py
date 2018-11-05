def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    now = len(nums) - 1
    i = now - 1
    while now > 0:
        while nums[i] >= (now - i) and i > 0:
            i -= 1
        now -= nums[i + 1]
        if i == 0 and nums[0] < now:
            return False

    return True


a=canJump([3,2,1,0,4])