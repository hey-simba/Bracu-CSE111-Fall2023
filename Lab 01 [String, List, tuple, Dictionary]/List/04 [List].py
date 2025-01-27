
#Task4
flag= True
while True:
  p=input()
  if p=="STOP":
    break
  else:
    p=p.split()
  for i in range(len(p)):
    p[i]=int(p[i])
  diff=len(p)-1

  for i in range(len(p)-1):
    if p[i]>p[i+1]:
      d= p[i]-p[i+1]
    else:
      d= p[i+1]-p[i]
    if d>diff:
      flag=False
  if flag:
    print("UB Jumper")
  else:
    print("Not UB Jumper")