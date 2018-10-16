def double_char(str):
  out = ""
  for i in range(len(str)):
    out += str[i] + str[i]
  return out