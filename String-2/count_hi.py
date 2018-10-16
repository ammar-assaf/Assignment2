def count_hi(str):
  count = 0
  for i in range(len(str)):
    if (i+1 != len(str)) and str[i] == 'h' and str[i+1] == 'i':
      count +=1
  return count