# -*- coding: utf-8 -*-
"""06 class

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/105q3d_LtCWy8f9KX-99mnZD5nUBuT_0D
"""

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