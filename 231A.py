-- Team ---
problems = int(input())
count = 0
for _ in range(problems):
    petya, vasya, tonya = map(int, input().split())
    sum = petya + vasya + tonya
    if sum >= 2:
        count += 1
print(count)
