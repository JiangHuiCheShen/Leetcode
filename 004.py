# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。
# #
# # 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

#思路：用额外的空间换取时间。从头按顺序比较nums1，nums2中的数，小的放到mergeList里面，于是一轮下来就排好序了，再根据奇偶来找
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    mergeList = []
    len1 = len(nums1)
    len2 = len(nums2)
    i = 0  #nums1的索引
    j = 0 #nums2的索引
    while i < len1 or j < len2:
        if i < len1 and j < len2:
            if (nums1[i] < nums2[j]):
                mergeList.append(nums1[i])
                i += 1
            else:
                mergeList.append(nums2[j])
                j += 1
        elif i == len1:    #只剩nums2的情况
            mergeList.append(nums2[j])
            j += 1
        elif j == len2:    #只剩nums1的情况
            mergeList.append(nums1[i])
            i += 1
    if (len1 + len2) % 2 == 0:
        return (mergeList[(len1 + len2) // 2 - 1] + mergeList[(len1 + len2) // 2]) / 2
    else:
        return mergeList[(len1 + len2 - 1) // 2]