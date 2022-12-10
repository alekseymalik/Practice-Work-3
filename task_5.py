import math

first = int(input("1: "))
second = int(input("2: "))
third = int(input("3: "))
forth = int(input("4: "))
list = {
    first:1,
    second:2,
    third:3,
    forth:4
}

print(f"{math.cos(min(list.keys()))}")