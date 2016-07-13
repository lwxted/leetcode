class Solution(object):
  def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # An attempt at implementing the karp-rabin algo
    p = 100000007
    ds = 256
    def hsh(s):
      v = 0
      for c in s:
        v = (v * ds + ord(c)) % p
      return v

    def hsh_incr(oh, l, oc, nc):
      v = 1
      for i in xrange(l - 1):
        v = (v * ds) % p
      return ((oh - ord(oc) * v) * ds + ord(nc)) % p

    needle_hash = hsh(needle)
    rolling_hash = hsh(haystack[:len(needle)])
    st = 0
    while st + len(needle) <= len(haystack):
      if rolling_hash == needle_hash:
        if haystack[st:st + len(needle)] == needle:
          return st
      if st + len(needle) == len(haystack):
        break
      rolling_hash = hsh_incr(
        rolling_hash, len(needle), haystack[st], haystack[st + len(needle)])
      st += 1
    return -1

print Solution().strStr('abcdef', 'cdff')
