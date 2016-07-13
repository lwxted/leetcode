class Solution(object):
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    def say(s):
      pc = s[0]
      n = 1
      l = []
      for c in s[1:]:
        if pc == c:
          n += 1
          continue
        l.append((pc, n))
        pc = c
        n = 1
      l.append((pc, n))
      return ''.join(str(n) + pc for (pc, n) in l)

    s = '1'
    i = 1
    while i < n:
      s = say(s)
      i += 1

    return s

print Solution().countAndSay(5)
