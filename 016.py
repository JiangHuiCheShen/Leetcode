class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        ans = nums[0:3]

        closesum = sum(ans)
        close = abs(closesum - target)
        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if abs(sums - target) < close:
                    close = abs(sums - target)
                    closesum = sums
                    # ans=[nums[i],nums[left],nums[right]]
                if sums == target:
                    return target
                elif sums < target:
                    left += 1
                else:
                    right -= 1

        return closesum

so=Solution()
ans=so.threeSumClosest([0,2,1,-3],1)