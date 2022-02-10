import numpy as np
import sys
import time

def do_computations(n):
    A = np.random.uniform(-1,1,(n, n))
    b = np.ones(n)

    for_loop_array = np.zeros(20)
    matmul_array = np.zeros(20)

    for iteration in range(20):
        C = np.zeros(n)
        start = time.perf_counter()
        for i in range(n):
            for j in range(n):
                C[i] += A[i][j] * b[j]
        end = time.perf_counter()
        for_loop_array[iteration] = (end - start)*1000

    print("For Loop Computations - ")
    print("Average: ", np.average(for_loop_array))
    print("Standard Deviation: ", np.std(for_loop_array))

    for iteration in range(20):
        start = time.perf_counter()
        
        C = np.matmul(A,b) 

        end = time.perf_counter()
        matmul_array[iteration] = (end - start)*1000

    print("Numpy Computations - ")
    print("Average: ", np.average(matmul_array))
    print("Standard Deviation: ", np.std(matmul_array))
    

if __name__=="__main__":
    n = int(sys.argv[1])
    do_computations(n)
