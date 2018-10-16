def big_diff(nums):
  minv = nums[0]
  maxv = nums[0]
  for i in range(len(nums)):
    minv = min(minv,nums[i])
    maxv = max(maxv,nums[i])
  return maxv - minv