# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution(object):
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    nl = []
    p1, p2 = l1, l2
    if p1 is None and p2 is None:
      return None
    while p1 and p2:
      if p1.val < p2.val:
        nl.append(p1)
        p1 = p1.next
      else:
        nl.append(p2)
        p2 = p2.next
    for i in xrange(len(nl) - 1):
      nl[i].next = nl[i + 1]
    if nl:
      nl[-1].next = p1 if p1 is not None else p2
      return nl[0]
    else:
      return p1 if p1 is not None else p2
