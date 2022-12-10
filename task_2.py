year = int(input("Number of year: "))

def choose_year(year):
    normal_year = 365
    visok_year = 366
    if year%4 == 0 and year % 100 != 0:
        print(visok_year)
    elif year%400 == 0:
        print(visok_year)
    else:
        print(normal_year)
choose_year(year)