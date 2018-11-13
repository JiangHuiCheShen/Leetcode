#编写一个函数来查找字符串数组中的最长公共前缀。
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs is []:
        return ''
    if len(strs)==1:
        return strs

    lenlists = []
    for i in range(len(strs)):
        lenlists.append(len(strs[i]))
    minlen = min(lenlists)
    common = ''
    i = 0
    j = 0

    while strs[0][j] == strs[i][j] and j < minlen:
        i += 1
        if i == len(strs):
            common += strs[0][j]
            i = 0
            j += 1

    return common


a=longestCommonPrefix(["flower"])
