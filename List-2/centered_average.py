def centered_average(nums):
  sum = 0
  maxv = max(nums)
  minv = min(nums)
  for i in range(len(nums)):
    sum += nums[i]
  return (sum -maxv-minv) / (len(nums)-2)