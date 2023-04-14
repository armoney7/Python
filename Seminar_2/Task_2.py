S = int(input("Введите сумму чисел S: "))
P = int(input("Введите произведение чисел P: "))

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == S and x * y == P:
            print(f"Задуманные числа: X = {x}, Y = {y}")
            break
    else:
        print("Подсказки неверны")       
    break
