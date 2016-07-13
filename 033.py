class Solution(object):
  def _searchRecursive(self, nums, target, st, ed):
    if st == ed:
      return -1
    if ed - st == 1:
      return st if nums[st] == target else -1
    mid = (st + ed) / 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      r = self._searchRecursive(nums, target, mid, ed)
      if r != -1:
        return r
      return self._searchRecursive(nums, target, st, mid)
    else:
      l = self._searchRecursive(nums, target, st, mid)
      if l != -1:
        return l
      return self._searchRecursive(nums, target, mid, ed)

  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return self._searchRecursive(nums, target, 0, len(nums))

print Solution().search([0], 2)
