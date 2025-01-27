

#Task2
user_input= input()
word=0
number=0
for i in user_input:
  if ord("A")<=ord(i)<=ord("Z") or ord("a")<=ord(i)<=ord("z"):
    word+=1
  elif chr(48)<=i<=chr(57):
    number+=1
if number==0:
  print("Word")
elif word==0:
  print("Number")
else:
  print("Mixed")