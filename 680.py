class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        first = True
        while left < right:
            if s[left] != s[right]:
                return self.valid(s[left + 1:right + 1]) or self.valid(s[left:right])  # 遇到不同时分两种情况

            left += 1
            right -= 1
        return True

    def valid(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

a=Solution()
a.validPalindrome("deeee")