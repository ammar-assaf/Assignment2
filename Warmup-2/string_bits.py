def string_bits(str):
  out = ""
  n =len(str)-1
  
  while n>=0:
    out += str[len(str) - n - 1]
    n-=2
  return out