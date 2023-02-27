import timeit


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


x = 0
while x < 30:
    start_time = timeit.default_timer()
    fibonacci(40)
    print(timeit.default_timer() - start_time)
    x += 1
