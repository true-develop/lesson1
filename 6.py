a = int(input("Введите результат пробежки"))
b = int(input("Введите общий желаемый результат"))
result_days = 1
while a < b:
    a *= 1.1
    result_days += 1
print(result_days)
