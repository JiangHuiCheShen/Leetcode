#给定一个没有重复数字的序列，返回其所有可能的全排列。
def backtracking(nums, rest, temp, ans):
    if rest == 0:

        ans.append(temp)
        return
    else:
        for i,value in enumerate(nums):
            if value not in temp:
                backtracking(nums, rest - 1, temp + [value], ans)
            # nums.append(value)
    return

def permute( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []

    backtracking(nums, len(nums), [], ans)

    return ans

test=permute([1,2,3])