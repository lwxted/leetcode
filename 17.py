class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dic = {
      2 : 'abc', 3 : 'def', 4 : 'ghi', 5 : 'jkl', 6 : 'mno', 7 : 'pqrs',
      8 : 'tuv', 9 : 'wxyz', 0 : ' '
    }
    if not len(digits):
      return []
    ans = ['']
    for d in digits:
      n_ans = []
      for c in dic[int(d)]:
        for e in ans:
          n_ans.append(e + c)
      ans = n_ans
    return ans

print Solution().letterCombinations('23')
