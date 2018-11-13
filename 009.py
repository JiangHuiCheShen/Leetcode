#判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    Tostr = str(x)
    i = 0
    length = len(Tostr)
    while i < length // 2:
        if Tostr[i] != Tostr[length - 1 - i]:
            return False
        i += 1
    return True