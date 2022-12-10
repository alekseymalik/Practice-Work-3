print("Вы покупаете шоколад по 5$ штуку.")
quest = int(input("Сколько штук: "))
sqrt = quest * 5
if quest >= 100:
    sqrt_per = sqrt - sqrt*1/10
    print("С вас", sqrt_per, "$")
else:
    print("С вас", sqrt,"$")