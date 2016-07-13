class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    ma = 0
    i, j = 0, len(height) - 1
    while i < j:
      ma = max(ma, (j - i) * min(height[i], height[j]))
      if height[i] < height[j]:
        i += 1
      else:
        j -= 1
    return ma
