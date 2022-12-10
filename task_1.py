a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
list = []
def one_three(a,b,c,list):
    if a == 1:
        list.append(a)
    elif a == 2:
        list.append(a)
    elif a == 3:
        list.append(a)
    else:
        print(f"Первый номер с числом ({a}) не подходит")
    if b == 1:
        list.append(b)
    elif b == 2:
        list.append(b)
    elif b == 3:
        list.append(b)
    else:
        print(f"Второй номер с числом ({b}) не подходит")
    if c == 1:
        list.append(c)
    elif c == 2:
        list.append(c)
    elif c == 3:
        list.append(c)
    else:
        print(f"Третий номер с числом ({c}) не подходит")
    print(f"Прошли такие числа: {list}")
one_three(a,b,c,list)