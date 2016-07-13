class Solution(object):
  def combinationRecur(self, candidates, left, st, curr, aggr):
    if left == 0:
      aggr.append(curr)
      return
    for i in xrange(st, len(candidates)):
      if i > st and candidates[i] == candidates[i - 1]:
        continue
      if candidates[i] > left:
        break
      self.combinationRecur(candidates, left - candidates[i], i + 1, curr + [candidates[i]], aggr)


  def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates = sorted(candidates)
    aggr = []
    curr = []
    self.combinationRecur(candidates, target, 0, curr, aggr)
    return aggr

print Solution().combinationSum2([2, 3, 4, 5, 7], 7)
