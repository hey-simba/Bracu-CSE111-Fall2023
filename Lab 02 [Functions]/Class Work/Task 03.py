
#Task 3
def replace_domain(email,new_domain,old_domain=None):
  index=0
  for char in range (len(email)):
    if email[char]=="@":
      index=char
      break
  if email[index+1: ]=="sheba.xyz":
      var= email
      print("Changed:",var)
  else:
      var=email[: index+1]+new_domain
      print("Unchnaged:",var)
replace_domain("bob@kaaj.com","sheba.xyz")