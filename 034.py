class Solution(object):
  def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def lb():
      lst, led = 0, len(nums)
      while True:
        if led - lst <= 1:
          return lst
        lmd = (lst + led) / 2
        if nums[lmd] < target:
          lst = lmd
        elif nums[lmd] > target:
          led = lmd
        else:
          if lmd - 1 >= 0 and nums[lmd - 1] == target:
            led = lmd
          else:
            return lmd

    def ub():
      ust, ued = 0, len(nums)
      while True:
        if ued - ust <= 1:
          return ust
        umd = (ust + ued) / 2
        if nums[umd] < target:
          ust = umd
        elif nums[umd] > target:
          ued = umd
        else:
          if umd + 1 < len(nums) and nums[umd + 1] == target:
            ust = umd + 1
          else:
            return umd

    lbr, ubr = lb(), ub()
    if nums[lbr] != target:
      return [-1, -1]
    return [lbr, ubr]

print Solution().searchRange([4, 6, 6, 7, 7, 7], 3)
