def backtracking(nums, rest, temp, ans, time, k):
    if rest == 0:
        ans.append(temp)
        return
        # return temp
    else:
        for i, value in enumerate(nums):
            if value not in temp:
                backtracking(nums, rest - 1, temp + [value], ans, time, k)
    return

def getPermutation( n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    ans = []
    nums = range(1, n + 1)
    backtracking(nums, len(nums), [], ans, 0, k)
    return ans

test=getPermutation(3,3)


