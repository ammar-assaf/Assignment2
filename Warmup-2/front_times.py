def front_times(str, n):
  out = ""
  if len(str) < 3:
    for i in range(n):
      out += str
  else:
    temp = str[0]+str[1]+str[2]
    for i in range(n):
      out+=temp
    
  return out