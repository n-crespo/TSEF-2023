import timeit


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = result
    return result


data = []
x = 0
while x < 30:
    start_time = timeit.default_timer()
    fibonacci(999)
    print(timeit.default_timer() - start_time)
    data.append(timeit.default_timer() - start_time)
    x += 1

print("mean = ", sum(data)/len(data))
