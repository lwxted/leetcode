class Solution(object):
  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while True:
      try:
        nums.remove(val)
      except:
        break
    return len(nums)

