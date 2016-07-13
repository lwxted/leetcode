class Solution(object):
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # Check rows
    for r in board:
      d = set()
      for ch in r:
        if ch == '.':
          continue
        if ch in d:
          return False
        d.add(ch)

    # Check cols
    for i in xrange(9):
      d = set()
      for j in xrange(9):
        ch = board[j][i]
        if ch == '.':
          continue
        if ch in d:
          return False
        d.add(ch)

    # Check grid
    for i in xrange(3):
      for j in xrange(3):
        d = set()
        for ii in xrange(3):
          for jj in xrange(3):
            ch = board[i * 3 + ii][j * 3 + jj]
            if ch == '.':
              continue
            if ch in d:
              return False
            d.add(ch)

    return True
