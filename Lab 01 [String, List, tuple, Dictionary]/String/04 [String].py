
#Task4
user_input1 = input()
user_input2= input()
common = ''
for i in user_input1:
  if i in user_input2:
    common += i
for i in user_input2:
  if i in user_input1 :
    common+=i
if len(common)==0:
  print("Nothing in common.")
else:
 print(common)