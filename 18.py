class Solution(object):
  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    d = dict()
    ans = set()
    nums = sorted(nums)
    for (i, e) in enumerate(nums):
      if e not in d:
        d[e] = []
      d[e].append(i)
    for i in xrange(len(nums)):
      for j in xrange(i + 1, len(nums)):
        for k in xrange(j + 1, len(nums)):
          r = target - nums[i] - nums[j] - nums[k]
          if r in d and d[r][-1] > k:
            ans.add((nums[i], nums[j], nums[k], r))
    return [list(s) for s in ans]

print Solution().fourSum([0, 0, 0, 0], 0)
