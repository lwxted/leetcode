class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    fl = []
    p = head
    while p is not None:
      fl.append(p)
      p = p.next
    if n == len(fl):
      return fl[0].next
    else:
      fl[-(n + 1)].next = fl[-n].next
      return head
