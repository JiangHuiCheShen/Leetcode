class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ab=''
        for i in s:
            if i.isdigit() or i.isalpha():
                ab+=i
        ab=ab.lower()
        left=0
        right=len(ab)-1
        while left<right:
            if ab[left]!=ab[right]:
                return False
            else:
                left+=1
                right-=1
        return True

sol=Solution()
a=sol.isPalindrome("A man, a plan, a canal: Panama")