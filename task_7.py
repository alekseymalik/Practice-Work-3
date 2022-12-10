print("--First triangle--")
first_ft = int(input("First side "))
first_st = int(input("Second side "))
first_tt = int(input("Third side "))
print("--Second triangle--")
second_ft = int(input("First side "))
second_st = int(input("Second side "))
second_tt = int(input("Third side "))
def first_triangle(first_ft, first_st, first_tt):
    P_F = first_ft + first_st + first_tt
    F_sqrt = P_F/2
    return (F_sqrt*(F_sqrt-first_ft)*(F_sqrt-first_ft)*(F_sqrt-first_tt))

def second_triangle(second_ft, second_st, second_tt):
    P_S = second_ft + second_st + second_tt
    S_sqrt = P_S / 2
    return (S_sqrt * (S_sqrt - second_ft) * (S_sqrt - second_st) * (S_sqrt - second_tt))
if first_triangle(first_ft, first_st, first_tt) == second_triangle(second_ft, second_st, second_tt):
    print(True)
else:
    print("Foul !!!")