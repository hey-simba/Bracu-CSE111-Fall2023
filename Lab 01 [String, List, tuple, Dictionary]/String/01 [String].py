
#Task one
user_input=input()
upper=""
lower=""
for i in range (len(user_input)):
  if ord("A")<=ord(user_input[i])<=ord("Z"):
    upper+=user_input[i]
  elif ord("a")<=ord(user_input[i])<=ord("z"):
    lower+=user_input[i]
if len(upper)>len(lower):
  upper1= user_input.upper()
  print(upper1)
elif len(lower)>=len(upper):
  lower1=user_input.lower()
  print(lower1)