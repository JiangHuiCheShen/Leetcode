class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k or num == '0':
            return '0'

        ans = [num[0]]
        for i in range(1, len(num)):

            if num[i] < ans[-1]:
                ans.pop()
                k -= 1
            ans.append(num[i])
            if k == 0:
                break
        if k > 0:
            ans = ans[:-k]
        else:
            ans += num[i + 1:]

        if ans[0] == '0':
            if len(ans) > 1:
                return ''.join(ans[1:])
            else:
                return '0'
        else:
            return ''.join(ans)
s=Solution()
s.removeKdigits("1234567890",9)