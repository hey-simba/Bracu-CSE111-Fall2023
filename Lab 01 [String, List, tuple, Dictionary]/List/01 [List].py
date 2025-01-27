
#Task1
li=[]
while True:
  inp=input()
  if inp=="STOP":
    break
  else:
    li.append(inp)
f=0
li1=[]
for i in range(len(li)):
  if li[i] not in li1:
    for j in range(len(li)):

      if li[i]==li[j]:
        f+=1
    print(f'{li[i]}:{f} times')
    f=0
  li1.append(li[i])