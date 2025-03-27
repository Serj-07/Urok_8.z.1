# Ввод числа N
N = int(input())

# Ввод N чисел и сохранение их в список
numbers = []
for _ in range(N):
    numbers.append(int(input()))

# Перевертывание списка
reversed_numbers = numbers[::-1]

# Вывод перевернутого списка
for number in reversed_numbers:
    print(number)

