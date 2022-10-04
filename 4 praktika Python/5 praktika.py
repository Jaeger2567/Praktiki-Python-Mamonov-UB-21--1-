counter = {}
for Иван in input().split():
    counter[Иван] = counter.get(Иван, 0) + 1
    print(counter[Иван] - 1, end=' ')
