# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1


#从头按顺序比较是否相等
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        start = 0
        if len(needle) > len(haystack):
            return -1

        while start <= len(haystack) - len(needle):
            i = start
            j = 0
            while haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return start
            start += 1
        return -1

#直接比较对应大小的数组是不是相等
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
            i += 1
        return -1