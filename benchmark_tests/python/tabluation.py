# A tail recursive function to
# calculate n th fibonacci number
def fib(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib(n - 1, b, a + b)


# Driver Code
n = 40
print("fib("+str(n)+") = "+str(fib(n)))
