

#Task 4
def show_palindrome(string):
  new_string=""
  for i in string:
    if i !=" ":
      new_string+=i

  reverse_string = new_string[ : :-1]
  if new_string==reverse_string:
      print("Palindrome")
  else:
      print("Not a palindrome")
inp=input()
show_palindrome(inp)