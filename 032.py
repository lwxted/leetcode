class Solution(object):
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    dp = [0] * len(s) # longest valid paren string len ending at this character
    m = 0
    for (i, c) in enumerate(s):
      if c == '(':
        continue
      # c == ')'
      if s[i - 1:i] == '(':
        dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
      elif s[i - 1:i] == ')':
        probe = i - dp[i - 1] - 1
        if probe < 0 or s[probe] == ')':
          continue
        dp[i] = 2 + dp[i - 1]
        if probe - 1 >= 0:
          dp[i] += dp[probe - 1]
      m = max(m, dp[i])
    print dp
    return m

print Solution().longestValidParentheses("()(())")
