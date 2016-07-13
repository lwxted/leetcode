#include <vector>
#include <unordered_set>
#include <utility>

using namespace std;

typedef vector<vector<char>> vvc;

class Solution {
private:
  bool isValidSudoku(vvc& board, int ci, int cj) {
    for (int i = 0; i < 9; ++i) {
      if (i != ci && board[ci][cj] == board[i][cj]) {
        return false;
      }
      if (i != cj && board[ci][cj] == board[ci][i]) {
        return false;
      }
    }
    for (int i = ci / 3 * 3; i < ci / 3 * 3 + 3; ++i) {
      for (int j = cj / 3 * 3; j < cj / 3 * 3 + 3; ++j) {
        if (i != ci && j != cj && board[ci][cj] == board[i][j]) {
          return false;
        }
      }
    }
    return true;
  }

  pair<int, int> nextPos(vvc& board, int ci, int cj) {
    while (ci < 9) {
      while (cj < 8) {
        ++cj;
        if (board[ci][cj] == '.') {
          return make_pair(ci, cj);
        }
      }
      cj = -1;
      ++ci;
    }
    return make_pair(ci, cj);
  }

  bool solveRecursive(vvc& board, int ci, int cj) {
    if (ci == 9) {
      return true;
    }
    pair<int, int> p = nextPos(board, ci, cj);
    bool succ = false;
    for (int i = 0; i < 9; ++i) {
      board[ci][cj] = i + '1';
      if (!isValidSudoku(board, ci, cj)) {
        board[ci][cj] = '.';
        continue;
      }
      if (!solveRecursive(board, p.first, p.second)) {
        board[ci][cj] = '.';
        continue;
      }
      succ = true;
      break;
    }
    return succ;
  }

public:
  void solveSudoku(vvc& board) {
    pair<int, int> p = nextPos(board, 0, -1);
    solveRecursive(board, p.first, p.second);
  }
};
