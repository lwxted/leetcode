class Solution(object):
  def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = [n for n in nums if n > 0]
    if not l:
      return 1
    ll = max(len(l), max(l))
    diff = (ll + 1) * ll / 2 - sum(l)
    return len(l) + 1 if diff == 0 else diff
