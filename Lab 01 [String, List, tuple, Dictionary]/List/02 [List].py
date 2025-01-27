
#Task2
len=int(input())
max_sum=None
sum=0
max_li=[]
for i in range(len):

  inp=input().split()

  for j in inp:
    sum+=int(j)
  if max_sum==None:
    max_sum=sum
    max_li=inp
  elif sum>max_sum:
    max_sum=sum

    max_li=inp
  sum=0
li=[]
for i in max_li:
    li.append(int(i))
print(max_sum)
print(li)