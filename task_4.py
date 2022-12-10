m = int(input("Число:"))
print("""
1 - Кілоограм
2 - мілі Грам
3 - Грам
4 - Тонна
5 - Центнер
""")
request_the_weight = int(input(":"))
if request_the_weight == 1:
    print(f"{m}kg")
if request_the_weight == 2:
    print(f"{m/1000000}kg")
if request_the_weight == 3:
    print(f"{m/1000}kg")
if request_the_weight == 4:
    print(f"{m/1000}kg")
if request_the_weight == 5:
    print(f"{m/100}kg")
