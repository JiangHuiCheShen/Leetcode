# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s2=list(s)
#         s2.reverse()
#         s2=''.join(s2)               #字符串反转
#         cell=[[0 for i in range(len(s2)+1)] for j in range(len(s)+1)]
#         maxlen=0
#         maxposition=0
#
#         for i in range(len(s)):
#             for j in range(len(s2)):
#                 if s[i]==s2[j]:
#                     cell[i+1][j+1]=cell[i][j]+1
#                     if (cell[i+1][j+1]>maxlen):    #还差一个约束条件，防止反转后的正好是原数据的一部分
#                         maxlen=cell[i+1][j+1]
#                         maxposition=i+1
#         return s[maxposition-maxlen:maxposition]
#
# longestPalindrome("fdgdfg")

#动态规划
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strings = len(s)
        if strings <= 1:
            return s
        mat = [[0 for i in range(strings)] for i in range(strings)]
        index_i = 0
        index_j = 0
        for i in range(strings):  # 单个字符
            mat[i][i] = 1

        for i in range(strings - 1):  # 两个字符情况
            j = i + 1
            if s[i] == s[j]:
                mat[i][j] = 1
                index_i = i
                index_j = j

        for length in range(2, strings):  # 多个字符情况
            for i in range(strings - length):
                j = i + length
                if s[i] == s[j] and mat[i + 1][j - 1] == 1:
                    mat[i][j] = 1
                    index_i = i
                    index_j = j
        return s[index_i:index_j + 1]

test=Solution()
a=test.longestPalindrome("cbbd")