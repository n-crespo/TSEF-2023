import timeit


def fibonacci(n):
    table = [0, 1]
    for i in range(2, n + 1):
        table.append(table[i-1] + table[i-2])
    return table[n]


data = []
x = 0
while x < 30:
    start_time = timeit.default_timer()
    # fibonacci(40)
    fibonacci(999)
    print(timeit.default_timer() - start_time)
    data.append(timeit.default_timer() - start_time)
    x += 1

print("mean = ", sum(data)/len(data))
