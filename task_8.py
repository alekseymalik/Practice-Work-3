b = int(input("Side: "))
h = int(input("Height: "))
def square(b, h):
    square_triangle = 1/2*b*h
    if square_triangle % 2 == 0:
        print(square_triangle/2)
    else:
        print("Не можу ділити на 2!")
square(b,h)