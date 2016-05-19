class Solution(object):
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0 or x < -(1 << 31) or x > (1 << 31) - 1:
      return 0
    absx = abs(x)
    sign = x / absx
    res = sign * int(str(absx)[::-1])
    if res < -(1 << 31) or res > (1 << 31) - 1:
      return 0
    return res
