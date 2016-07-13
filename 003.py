class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    d = dict()
    max_l = 0
    cut = 0
    for (i, c) in enumerate(s):
      if c in d and d[c] >= cut:
        cut = d[c] + 1
      d[c] = i
      max_l = max(max_l, i - cut + 1)
    return max_l

print Solution().lengthOfLongestSubstring('dvdf')


