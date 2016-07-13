class Solution(object):
  def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1:
      return
    i = len(nums) - 2
    while i >= 0:
      if nums[i] < nums[i + 1]:
        break
      i -= 1
    if i == -1:
      nums[:] = nums[::-1]
      return
    j = len(nums) - 1
    while j > i:
      if nums[j] > nums[i]:
        break
      j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = nums[i + 1:][::-1]


print Solution().nextPermutation([2, 1])
