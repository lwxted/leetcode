class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    rows = ['' for i in xrange(numRows)]
    r, d = 0, 1
    if numRows <= 1:
      return s
    for (i, c) in enumerate(s):
      rows[r] += c
      r = r + d
      if r == numRows:
        r, d = numRows - 2, -1
      elif r == -1:
        r, d = 1, 1
    return ''.join(rows)

print Solution().convert("PAYPALISHIRING", 3)
