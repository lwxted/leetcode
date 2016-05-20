class Solution(object):
  def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    def genParenRecur(ol, cl, cs, ps):
      if cl == ol == 0:
        ps.append(cs)
        return
      if ol > 0:
        genParenRecur(ol - 1, cl, cs + '(', ps)
      if cl > ol:
        genParenRecur(ol, cl - 1, cs + ')', ps)

    ps = []
    genParenRecur(n, n, '', ps)
    return ps

print Solution().generateParenthesis(4)
