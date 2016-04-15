class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    d = set(nums)
    for (i, e) in enumerate(nums):
      if target - e in d:
        nums[i] = None
        if target - e not in nums:
          continue
        return sorted([i, nums.index(target - e)])
    return []
