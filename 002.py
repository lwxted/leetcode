# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    n1, n2, i1, i2 = 0, 0, 0, 0
    while l1:
      n1 += l1.val * 10 ** i1
      i1 += 1
      l1 = l1.next
    while l2:
      n1 += l2.val * 10 ** i2
      i2 += 1
      l2 = l2.next
    a = n1 + n2
    r = ListNode(0)
    p = r
    while a:
      p.val = a % 10
      a /= 10
      if a != 0:
        p.next = ListNode(0)
        p = p.next
      else:
        break
    return r

