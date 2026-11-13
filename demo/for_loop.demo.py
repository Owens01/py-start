data = ["age", "owen", 3, 10, "python"]

# for printing all the values in arr
for list in data:
    print(list)

# for printing few
for values in range(5):
    print(values)

# using break & continue
for num in range(20):
    if num % 4 == 0:
        continue
    if num == 10:
        break
    print(num)
