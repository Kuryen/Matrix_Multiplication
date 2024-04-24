import time
import numpy as np
import multiprocessing as mp
import threading

def Mat_Mult_S(MAT_A, MAT_B):
    MAT_C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(B.shape[0]):
                MAT_C[i, j] += MAT_A[i, k] * MAT_B[k, j]
    return MAT_C

def Mat_Mult_P(MAT_A, MAT_B, nPROC):
    MAT_C = np.zeros((A.shape[0], B.shape[1]))
    Threads = [0 for _ in range(nPROC)]
    for PROC in range(nPROC):
        Threads[PROC] = threading.Thread(target=Sub_Mat_Mult_P, args=(MAT_A, MAT_B, MAT_C, PROC, nPROC))
    for Thread in Threads:
        Thread.start()
    for Thread in Threads:
        Thread.join()
    return MAT_C

def Sub_Mat_Mult_P(MAT_A, MAT_B, MAT_C, PROC, nPROC):
    for i in range(PROC, A.shape[0], nPROC):
        for j in range(B.shape[1]):
            for k in range(B.shape[0]):
                MAT_C[i, j] += MAT_A[i, k] * MAT_B[k, j]

if __name__ == '__main__':

    nlist = [100, 1000, 5000, 10000]
    pList = [1, 2, 4, 8]
    t = 0

    for e_n in nlist:

        print("\nCalculating for", e_n, "x", e_n, "Matrix")

        n = e_n
        m = n
        l = n

        A = np.random.randint(0, 10, size=(n, m))
        print(A, "\n")

        B = np.random.randint(0, 10, size=(m, l))
        print(B, "\n")

        for e_p in pList:

            print("\nNumber of Processes:", e_p)

            p = e_p

            if e_p is 1:
                t1_o = time.time()
                C = Mat_Mult_S(A, B)
                t1_f = time.time()
                t = t1_f - t1_o
                print("Time:", t1_f - t1_o)
                print(C, "\n")

            else:
                t2_o = time.time()
                D = Mat_Mult_P(A, B, p)
                t2_f = time.time()
                su = (t - (t2_f - t2_o)) / t
                print("Time:", t2_f - t2_o)
                print("Speed Up:", su)
                print(D, "\n")
