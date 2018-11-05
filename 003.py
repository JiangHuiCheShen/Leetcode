#给定一个字符串，找出不含有重复字符的最长子串的长度。

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    strdict = {}   #字典存放已有的字母和新的位置
    start = 0      #目前窗口开头
    end = 0        #目前窗口末尾
    maxlen = 0
    for i in range(len(s)):
        if s[i] in strdict and strdict.get(s[i]) >= start:   #遇到有重复的并且其在字典里的位置要在目前窗口start之后。不然就会将start位置弄到前面了如abba
            start = strdict.get(s[i]) + 1
        end = i
        strdict[s[i]] = i  #更新位置

        max_len = max(maxlen, end - start + 1)

    return maxlen


s='abba'
len=lengthOfLongestSubstring(s)
print(len)

a=list(range(1,1000))
import time
start=time.time()
for i,name in enumerate(a):        # 这样索引比较快
    print(i,name)
end=time.time()
print(end-start)

start=time.time()
for i in range(len(a)):
    print(i,a[i])
end = time.time()
print(end - start)

