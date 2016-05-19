class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    ma = 0
    for i in xrange(0, len(height)):
      for j in xrange(i + 1, len(height)):
        ma = max(ma, (j - i) * min(height[i], height[j]))
    return ma
