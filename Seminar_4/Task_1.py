import random

n, m = int(input("Введите количество элементов первого множества: ")), int(input("Введите количество элементов второго множества: "))

set1, set2 = {random.randint(1, 100) for i in range(n)}, {random.randint(1, 100) for i in range(m)}

print(f"Первое множество: {set1}\nВторое множество: {set2}")

intersection = sorted(set1 & set2)
print("Числа, встречающиеся в обоих наборах:")
print(", ".join(str(x) for x in intersection) + ".")
