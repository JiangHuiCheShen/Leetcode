class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '':
            return 0
        if str == '-' or str == '+':
            return 0

        if not (str[0].isdigit() or str[0] == '-' or str[0] == '+' or str[0]== ' '):
            return 0
        i = 0
        syb = 1
        while i < len(str) and str[i] == ' ':
            i += 1
        while i < len(str) and not str[i].isdigit():
            if str[i] == '-':
                syb *= -1
            i += 1
        num = 0
        while i < len(str) and str[i].isdigit():
            num *= 10
            num += int(str[i])
            i += 1
        return num * syb

s=Solution()
s.myAtoi("+-2")