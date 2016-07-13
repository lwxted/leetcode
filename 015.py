class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    d = dict()
    nums = sorted(nums)
    for (i, e) in enumerate(nums):
      if e not in d:
        d[e] = []
      d[e].append(i)
    ans = set()
    for i in xrange(len(nums)):
      for j in xrange(i + 1, len(nums)):
        if -(nums[i] + nums[j]) in d and d[-(nums[i] + nums[j])][-1] > j:
          ans.add((nums[i], nums[j], -(nums[i] + nums[j])))
    return [list(t) for t in ans]

print Solution().threeSum([-1, 0, 1, 2, -1, -4])
