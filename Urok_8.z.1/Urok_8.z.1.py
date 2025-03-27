
N = int(input())


numbers = []
for _ in range(N):
    numbers.append(int(input()))


reversed_numbers = numbers[::-1]

for number in reversed_numbers:
    print(number)

