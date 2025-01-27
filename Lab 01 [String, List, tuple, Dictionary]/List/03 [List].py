
#Task3
inp1=input().split()
inp2=input().split()
li=[]
li1=[]
li2=[]
for i in inp1:
    li1.append(int(i))
for j in inp2:
    li2.append(int(j))
print(li1)
print(li2)
for x in li1:
  for y in li2:
    ele= x*y
    li.append(ele)
print(li)