

def is_james_bond(li):
    james_bond= False
    position = 1
    for num in li:
        if num == 0 and position < 3:
            position += 1
        elif num == 7 and position == 3:
            james_bond= True
    return james_bond
result=is_james_bond( [1, 7, 2, 0, 4, 5, 0] )
print(result)