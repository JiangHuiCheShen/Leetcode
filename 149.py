def maxgys(dividend, divisor):
    if dividend%divisor==0:
        return divisor
    else:
        return  maxgys(divisor,dividend%divisor)

teat=maxgys(-10,2)