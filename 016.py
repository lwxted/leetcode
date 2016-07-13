class Solution(object):
  def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # O(N^2)
    nums = sorted(nums)
    c = nums[-1] + nums[-2] + nums[-3]
    for i in xrange(0, len(nums)):
      j, k = i + 1, len(nums) - 1
      while j < k:
        s = nums[i] + nums[j] + nums[k]
        if abs(target - s) < abs(target - c):
          c = s
        if s < target:
          j += 1
        else:
          k -= 1
    return c

    # O(N^2 log N)?
    # nums = sorted(nums)
    # closest_diff, closest_sum = sum(nums[-1:-4:-1]), 0
    # for i in xrange(len(nums)):
    #   for j in xrange(i + 1, len(nums)):
    #     t = target - nums[i] - nums[j]
    #     lo, hi = j + 1, len(nums)
    #     while lo < hi:
    #       mid = (lo + hi) / 2
    #       if nums[mid] > t:
    #         hi = mid
    #       elif nums[mid] == t:
    #         break
    #       else:
    #         if mid + 1 >= len(nums) or nums[mid + 1] > t:
    #           break
    #         if nums[mid + 1] < t:
    #           lo = mid + 1
    #         else:
    #           mid += 1
    #           break
    #     midl = mid
    #     olo, lo, hi = j + 1, j + 1, len(nums)
    #     while lo < hi:
    #       mid = (lo + hi) / 2
    #       if nums[mid] < t:
    #         lo = mid + 1
    #       elif nums[mid] == t:
    #         break
    #       else:
    #         if mid - 1 < olo or nums[mid - 1] < t:
    #           break
    #         if nums[mid - 1] > t:
    #           hi = mid - 1
    #         else:
    #           mid -= 1
    #           break
    #     midr = mid
    #     if j < midl and abs(t - nums[midl]) < closest_diff:
    #       closest_diff, closest_sum = abs(t - nums[midl]), nums[i] + nums[j] + nums[midl]
    #     if j < midr and abs(t - nums[midr]) < closest_diff:
    #       closest_diff, closest_sum = abs(t - nums[midr]), nums[i] + nums[j] + nums[midr]
    # return closest_sum

print Solution().threeSumClosest([0, 1, 1, 1], -100)
