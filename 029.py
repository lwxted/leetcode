class Solution(object):
  def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == -2147483648 and divisor == -1:
      return 2147483647

    n_dvd = (abs(dividend) + dividend == 0)
    n_dsr = (abs(divisor) + divisor == 0)

    d_sgn = n_dvd ^ n_dsr

    dividend = abs(dividend)
    divisor = abs(divisor)

    # muls[i] = 2^i * divisor
    muls = [divisor]
    cnt = [1]
    while muls[-1] < dividend:
      muls.append(muls[-1] + muls[-1])
      cnt.append(cnt[-1] + cnt[-1])
    res = 0
    while dividend >= divisor:
      lo = 0
      hi = len(cnt)
      while lo < hi - 1:
        mid = (lo + hi) / 2
        if muls[mid] == dividend:
          break
        elif muls[mid] < dividend:
          lo = mid
        else:
          hi = mid
      res += cnt[lo]
      dividend -= muls[lo]
    return -res if d_sgn else res

print Solution().divide(-1, -1)
