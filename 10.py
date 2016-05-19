class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    dp = [[None for i in xrange(len(p))] for j in xrange(len(s) + 1)]

    def isMatchHelper(ss, ps):
      if ps >= len(p):
        return ss >= len(s)
      if ss >= len(s):
        for c in xrange(ps, len(p), 2):
          if p[c + 1:c + 2] != '*':
            dp[ss][ps] = False
            return False
        dp[ss][ps] = True
        return True

      if dp[ss][ps] is not None:
        return dp[ss][ps]
      if p[ps + 1:ps + 2] != '*':
        if p[ps] == '.':
          dp[ss][ps] = isMatchHelper(ss + 1, ps + 1)
          return dp[ss][ps]
        dp[ss][ps] = p[ps] == s[ss] and isMatchHelper(ss + 1, ps + 1)
        return dp[ss][ps]
      else:
        if isMatchHelper(ss, ps + 2):
          dp[ss][ps] = True
          return dp[ss][ps]
        for i in xrange(ss + 1, len(s) + 1):
          if p[ps] != '.':
            if s[i - 1] != p[ps]:
              break
          if isMatchHelper(i, ps + 2):
            dp[ss][ps] = True
            return dp[ss][ps]
        dp[ss][ps] = False
        return False

    return isMatchHelper(0, 0)

print Solution().isMatch("a", "ab*")
