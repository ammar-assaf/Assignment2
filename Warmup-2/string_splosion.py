def string_splosion(str):
  out = ""
  i = 0
  while i<=len(str):
    out+= str[:i]
    i+=1
  return out