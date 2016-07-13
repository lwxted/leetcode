# class Solution(object):
#   def findSubstring(self, s, words):
#     """
#     :type s: str
#     :type words: List[str]
#     :rtype: List[int]
#     """
#     def verify(concat, words):
#       wd_set = dict()
#       for w in words:
#         if w not in wd_set:
#           wd_set[w] = 0
#         wd_set[w] += 1
#       for i in xrange(0, len(concat), len(words[0])):
#         if concat[i:i + len(words[0])] not in wd_set:
#           return False
#         mword = concat[i:i + len(words[0])]
#         wd_set[mword] -= 1
#         if wd_set[mword] == 0:
#           del wd_set[mword]
#       return not wd_set

#     tlen = sum(len(w) for w in words)

#     if not words or not s or tlen > len(s):
#       return []

#     d = {c : 0 for c in ''.join(words)}
#     rd = {c : 0 for c in ''.join(words)}
#     res = []
#     for w in words:
#       for c in w:
#         rd[c] += 1
#     for i in xrange(0, tlen):
#       if s[i] in d:
#         d[s[i]] += 1
#     if d == rd and verify(s[0:tlen], words):
#       res.append(0)
#     for i in xrange(0, len(s) - tlen):
#       if s[i] in d:
#         d[s[i]] -= 1
#       if s[i + tlen] in d:
#         d[s[i + tlen]] += 1
#       if d == rd and verify(s[i + 1:i + tlen + 1], words):
#         res.append(i + 1)
#     return res

class Solution(object):
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    rtn = []
    freq = dict()
    for word in words:
      if word not in freq:
        freq[word] = 0
      freq[word] += 1
    for i in xrange(0, len(s) - len(words) * len(words[0]) + 1):
      j = i
      stat = freq.copy()
      for j in xrange(i, i + len(words) * len(words[0]), len(words[0])):
        ss = s[j:j + len(words[0])]
        if ss in stat and stat[ss] > 0:
          stat[ss] -= 1
        else:
          break
      thru = True
      for k in stat:
        if stat[k] > 0:
          thru = False
          break
      if thru:
        rtn.append(i)
    return rtn


print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
