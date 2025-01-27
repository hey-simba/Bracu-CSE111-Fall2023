

def assign_students_to_sections(sections, *names):
  names= list(names)

  di={}
  for i in range (len(sections)):
    di[sectons[i]]= []

  for i in names:
    sum=0
    for j in range (len(i)):
      sum+=ord(j)
    mod = sum%5
  for i in range (len(names)):
    for j in range (len(sections)):
     if mod==i:
       if sections[i] not in di:
         di[sections[i]]= [names[j]]