cost = int(input("Cost: "))
def normal(cost):
    print(cost)
def three_percent(cost):
    three_percent = 3 / 100
    percent_of_result = cost*three_percent
    print(cost-percent_of_result)
def five_percent(cost):
    five_percent = 5 / 100
    percent_of_result = cost * five_percent
    print(cost-percent_of_result)
def quest(cost):
    if 1000 > cost >= 500:
        three_percent(cost)
    if cost >= 1000:
        five_percent(cost)
    if cost < 500:
        normal(cost)
quest(cost)