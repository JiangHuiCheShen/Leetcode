
#给定一个 32 位有符号整数，将整数中的数字进行反转。

#join 和split 的用法  字符串和list互转
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    res = list(str(x))
    res.reverse()
    if res[-1] == '-':
        result = int('-' + ''.join(res[0:-1]))
    else:
        result = int(''.join(res))
    # if -2 ** 31 <= result <= 2 ** 31 - 1:
    if result.bit_length()<32:   #获取内存二进制的长度
        return result
    else:
        return 0