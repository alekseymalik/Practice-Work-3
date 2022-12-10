import math

first = int(input("1: "))
second = int(input("2: "))
third = int(input("3: "))

list = {
    first:1,
    second:2,
    third:3,

}

print(f"{math.cos(max(list.keys()))}")