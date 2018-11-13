class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        stack = []

        ans = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)


            else:
                if stack == []:
                    start = i + 1
                else:
                    m = stack.pop()
                    if stack == []:
                        ans = max(ans, i - start + 1)
                    else:
                        ans = max(ans, i - m + 1)

        return ans

a=Solution()
a.longestValidParentheses('(()')