# import random
# import time

# def sort_array(array):
#     start = time.time()
#     array.sort()
#     end = time.time()
#     return end - start

# x=0
# while x<30:
#     array = [random.randint(0, 100000) for _ in range(100000)]
#     elapsed_time = sort_array(array)
#     print(f"Sorting the array took {elapsed_time:.2f} seconds.")
#     x += 1

# -------------------------------------------------------------------


# import time

# def matrix_multiplication(size):
#     start = time.time()
#     A = [[0.0 for j in range(size)] for i in range(size)]
#     B = [[0.0 for j in range(size)] for i in range(size)]
#     C = [[0.0 for j in range(size)] for i in range(size)]
#     for i in range(size):
#         for j in range(size):
#             A[i][j] = i * j
#             B[i][j] = i + j
#     for i in range(size):
#         for j in range(size):
#             for k in range(size):
#                 C[i][j] += A[i][k] * B[k][j]
#     end = time.time()
#     return end - start

# if __name__ == "__main__":
#     size = 2000
#     elapsed_time = matrix_multiplication(size)
#     print(f"Matrix multiplication of size {size} took {elapsed_time:.2f} seconds.")

import time
import numpy as np

def matrix_multiplication(size):
    start = time.time()
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    C = np.dot(A, B)
    end = time.time()
    return end - start

if __name__ == "__main__":
    size = 2000
    elapsed_time = matrix_multiplication(size)
    print(f"Matrix multiplication of size {size} took {elapsed_time:.2f} seconds.")
