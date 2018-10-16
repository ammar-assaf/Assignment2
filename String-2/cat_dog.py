def cat_dog(str):
  countC = 0
  countD = 0
  for i in range(len(str)-2):
    if (str[i] == 'c' and str[i+1] == 'a'and str[i+2] == 't'):
      countC +=1
    if (str[i] == 'd' and str[i+1] == 'o'and str[i+2] == 'g'):
      countD +=1
  return countC == countD