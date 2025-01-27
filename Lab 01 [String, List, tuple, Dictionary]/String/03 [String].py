

#Task 3
string=input()
upper1=0
upper2=0
for i in range (len(string)):
  if string[i].isupper():
    upper1= i
    break
for j in range (upper1,len(string)):
  if string[j].isupper() and j!= upper1:
    upper2= j
    break

lower= string[upper1+1:upper2]

if len(lower)== 0:
  print('BLANK')
else:
  print(lower)