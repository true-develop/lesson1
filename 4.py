numb = int(input("Введите целое положительное число >>>"))
max_numb = 0
while numb > 0:
    c = numb % 10
    if c >= max_numb:
        max_numb = c
    numb //= 10
    print("Максимальное число", max_numb)
