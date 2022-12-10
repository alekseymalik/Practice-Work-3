x = int(input("x: "))
y = int(input("y: "))
R = int(input("R: "))
if R*(-1) < x < R and R*(-1) < y < R:
    print(f"x: {x}, y: {y}, в кругу")
else:
    print(f"x: {x}, y: {y}, не в кругу")
