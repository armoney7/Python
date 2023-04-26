import random

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = {random.randint(1, 100) for i in range(n)}

set2 = {random.randint(1, 100) for i in range(m)}

print("Первое множество:", set1)
print("Второе множество:", set2)

intersection = sorted(set1 & set2)
print("Числа, встречающиеся в обоих наборах:")
print(", ".join(str(x) for x in intersection))
