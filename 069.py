# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        num=(x.bit_length()-1)//2
        while num**2 <=x:
            num+=1
        return num-1

#二分法  一开始设置除数为x的一半，
def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if x // mid == mid:
            return mid
        if x // mid < mid:
            right = mid - 1
        else:
            left = mid + 1
    return right