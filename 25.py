# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  def __repr__(self):
    return str(self.val)

class Solution(object):
  def reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    nl, p = [], head
    if head is None:
      return None
    while p is not None:
      nl.append(p)
      p = p.next
    for i in xrange(0, len(nl) / k):
      if i * k + k - 1 < len(nl):
        nl[i * k : i * k + k] = nl[i * k : i * k + k][::-1]
    for i in xrange(0, len(nl) - 1):
      nl[i].next = nl[i + 1]
    nl[-1].next = None
    return nl[0]


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
Solution().reverseKGroup(a, 2)
