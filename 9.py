class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
      return False
    return int(''.join(str(x)[::-1])) == x
