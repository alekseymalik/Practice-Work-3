import math
x = int(input("x: "))
y = int(input("y: "))
# geo_middle = math.sqrt(x*y)
aref_middle = (x+y)/2
# if x and y > 0:
#     print(geo_middle)
# elif x and y < 0:
#     print(geo_middle)
# else:
#     print(aref_middle)
list_pos = []
list_neg = []
if x >= 0:
    list_pos.append(x)
if x < 0:
    list_neg.append(x)
if y >= 0:
    list_pos.append(y)
if y < 0:
    list_neg.append(y)
# print(list_neg)
# print(list_pos)
# print(len(list_neg))
# print(len(list_pos))
if len(list_pos) == 2:
    print(math.sqrt(x*y))
elif len(list_neg) == 2:
    print(math.sqrt(x*y))
elif len(list_pos) == 1:
    print(aref_middle)
