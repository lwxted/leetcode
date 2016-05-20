class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i, p = 0, None
    while i < len(nums):
      if p == nums[i]:
        del nums[i]
        continue
      p = nums[i]
      i += 1
    return len(nums)


a = [1, 1, 1, 2, 3]
print Solution().removeDuplicates(a)
print a
