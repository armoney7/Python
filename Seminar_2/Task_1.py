n = int(input("Введите количество монеток: "))

reshka_count = 0
orel_count = 0

for i in range(n):
    coin = input(f"Введите сторону монеты {i+1} (решка/орел): ")

    if coin == "решка":
        reshka_count += 1
    elif coin == "орел":
        orel_count += 1

min_flips = min(reshka_count, orel_count)

print(f"Минимальное количество монет, которые нужно перевернуть: {min_flips}")
