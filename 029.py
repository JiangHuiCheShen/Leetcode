# def divide(dividend, divisor):
#     """
#     :type dividend: int
#     :type divisor: int
#     :rtype: int
#     """
#     abs_flag = 0
#     if dividend < 0 and divisor > 0:
#         dividend = abs(dividend)
#         abs_flag = 1
#     if dividend > 0 and divisor < 0:
#         divisor = abs(divisor)
#         abs_flag = 1
#
#     if divisor <= dividend:
#         ans = 0
#     else:
#         return 0
#     temp=divisor
#     while temp <= dividend:
#         temp += divisor
#         ans += 1
#
#     if abs_flag:
#         return ans - ans - ans
#     else:
#         return ans
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if not -(2**31)<dividend<=2**31-1:
        return 2147483647
    abs_flag = 0
    if dividend < 0 and divisor > 0:
        dividend = abs(dividend)
        abs_flag = 1
    if dividend > 0 and divisor < 0:
        divisor = abs(divisor)
        abs_flag = 1
    now=dividend
    ans=0
    while now>=divisor:         #剩余的被除数比除数大就继续
        j=0
        temp = divisor
        while temp<=now:        #被除数一直左移直到比当前的被除数要大
            temp=temp<<1
            j+=1
        ans=ans+2**(j-1)
        now=now-(temp>>1)         #剩余的被除数减去比它小的除数

    return ans-ans-ans if abs_flag else ans



ans=divide(-2147483648,-1)