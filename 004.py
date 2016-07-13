class Solution(object):
  def findIndex(self, nums1, nums2, k):
    if not nums2:
      return nums1[k]
    if not nums1:
      return nums2[k]
    if k <= 1:
      return sorted(nums1[0:2] + nums2[0:2])[k]
    ind = k / 2 - 1
    n1 = nums1[min(len(nums1) - 1, ind)]
    n2 = nums2[min(len(nums2) - 1, ind)]
    if n1 < n2:
      return self.findIndex(nums1[ind + 1:], nums2, k - min(len(nums1) - 1, ind) - 1)
    else:
      return self.findIndex(nums1, nums2[ind + 1:], k - min(len(nums2) - 1, ind) - 1)

  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if (len(nums1) + len(nums2)) % 2:
      return float(self.findIndex(nums1, nums2, (len(nums1) + len(nums2)) / 2))
    else:
      return float(
        self.findIndex(nums1, nums2, (len(nums1) + len(nums2)) / 2) +
        self.findIndex(nums1, nums2, (len(nums1) + len(nums2)) / 2 - 1)) / 2

print Solution().findMedianSortedArrays([5], [1, 2, 3, 4, 6, 7, 8])
