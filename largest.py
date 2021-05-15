def largest(a,b,c):
  if(a>b):
    if(a>c):
      return a
  elif(b>c):
    return b
  else:
    return c
   
print(largest(3,2,1))
