def close_far(a, b, c):
  if abs(a-b) <= 1 and not abs(b-c) <= 1 and not abs(a-c) <=1:
    return True
  elif abs(a-c) <= 1 and not abs(c-b) <= 1 and not abs(a-b) <=1:
    return True
  else:
    return False