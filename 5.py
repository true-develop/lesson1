profit = int(input("Введите выручку вашей фирмы: "))
costs = int(input("Введите издержки вашей фирмы:"))
if profit > costs:
    print(f"Рентабельность выручки= {profit/costs: .2f} ")
    worker = int(input("Введите количество сотрудников в фирме: "))
    print(f"Прибыль на одного сотрудника= {profit/worker} ")
elif profit == costs:
    print("Фирма работает в плюс")
else:
    print("Фирма работает в убыток")