class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    op = '([{'
    cl = ')]}'

    st = []
    for c in s:
      if c in op:
        st.append(c)
      else:
        if st and op.index(st[-1]) == cl.index(c):
          st.pop()
        else:
          return False
    return not st

print Solution().isValid(']')
