class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [nums[0]]
        for i in range(1,len(nums)):
            if len(ans) < 3:
                if nums[i] > ans[-1]:
                    ans.append(nums[i])
                elif ans[0] < nums[i] < ans[-1]:
                    ans.insert(1, nums[i])
                elif ans[0] > nums[i]:
                    ans.insert(0, nums[i])
            else:
                if nums[i] > ans[2]:
                    ans[0]=ans[1]
                    ans[1]=ans[2]
                    ans[2] = nums[i]
                elif ans[1] < nums[i] < ans[2]:
                    ans[0]=ans[1]
                    ans[1] = nums[i]
                elif ans[0] < nums[i] < ans[1]:
                    ans[0] = nums[i]

        if len(ans) < 3:
            return ans[-1]
        return ans[0]

s=Solution()
ans=s.thirdMax([3,3,3,3,4,3,2,3,3])