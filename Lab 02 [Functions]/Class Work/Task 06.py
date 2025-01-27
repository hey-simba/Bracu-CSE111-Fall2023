
#Task 6
def func(s):

    li = s.split()
    symbols = ['.', '?', '!']
    ans = ""
    found = False

    for i in range(len(li)):
        word = ""
        for j in range(len(li[i])):
            if (i == 0 and j == 0) or found == True or (len([li[i]]) == 1 and li[i] == 'i'):
                word += li[i][j].upper()
            else:
                word += li[i][j]

            if li[i][j] in symbols:
                found = True
            else: found = False
        ans += word + " "
    print(ans)

s = input()
func(s)