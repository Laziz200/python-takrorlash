numbers = [1, 2, 33, 5, 6, 7, 7]
d = int(input("son kiriting: "))

indices = set()
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == d:
            indices.add((i, j))
print(indices)
for index_pair in indices:
    print(index_pair)