class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans=''
        nums=[i for i in range(1,n+1)]
        import math
        yushu=k
        for i in range(n-1,-1,-1):
            fac=math.factorial(i)
            index=yushu//fac
            yushu=yushu%fac
            if yushu==0:
                index-=1
            ans += str(nums[index])
            nums.remove(nums[index])

        return ans

test=Solution()
a=test.getPermutation(5,3)