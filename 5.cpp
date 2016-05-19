#include <string>
#include <iostream>

using namespace std;

class Solution {
private:
  int dp[1001][1001];

public:
  int isPalindrome(const string& s, int sti, int edi)
  {
    if (dp[sti][edi] != -1) return dp[sti][edi];
    if (sti > edi) return 1;
    dp[sti][edi] = (int) (s[edi] == s[sti] && isPalindrome(s, sti + 1, edi - 1));
    return dp[sti][edi];
  }


  string longestPalindrome(string s)
  {
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < s.size(); ++i) {
      dp[i][i] = 1;
    }
    int max_sti = -1, max_edi = -1, max_len = 0;
    for (int i = 0; i < s.size(); ++i) {
      for (int j = i; j < s.size(); ++j) {
        if (isPalindrome(s, i, j) && j - i + 1 > max_len) {
          max_sti = i;
          max_edi = j;
          max_len = j - i + 1;
        }
      }
    }
    return s.substr(max_sti, max_len);
  }
};

int main()
{
  Solution s;
  std::cout << s.longestPalindrome("lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc") << std::endl;
}
