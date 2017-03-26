f = [1, 1]
n = 0

while n < 10:
    f.append(f[-1] + f[-2])
    n += 1


for item in f:
    print(item)
