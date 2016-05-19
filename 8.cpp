class Solution {
public:
  int myAtoi(string str) {
    if (str.empty())
      return 0;
    istringstream iss(str);
    int i;
    iss >> i;
    return i;
  }
};
