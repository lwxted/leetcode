class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
      return ''
    cnt = 0
    broke = False
    while not broke:
      for s in strs:
        if len(s) <= cnt or s[cnt] != strs[0][cnt]:
          return strs[0][:cnt]
      cnt += 1

print Solution().longestCommonPrefix(['ab', 'aba'])
