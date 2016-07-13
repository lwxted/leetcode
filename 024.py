# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
      return None
    if head.next is None:
      return head
    a, b, head, p = head, head.next, head.next, None
    while a and b:
      a.next = b.next
      b.next = a
      if p:
        p.next = b
      a, b, p = a.next, a.next.next if a.next is not None else None, a
    if a and not b:
      p.next = a
    return head
