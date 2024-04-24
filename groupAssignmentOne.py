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
    pool = mp.Pool(processes=nPROC)
    for PROC in range(nPROC):
        pool.apply_async(Sub_Mat_Mult_P, args=(MAT_A, MAT_B, MAT_C, PROC, nPROC))
    pool.close()
    pool.join()
    return MAT_C

def Sub_Mat_Mult_P(MAT_A, MAT_B, MAT_C, PROC, nPROC):
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(PROC, B.shape[0], nPROC):
                MAT_C[i, j] += MAT_A[i, k] * MAT_B[k, j]

if __name__ == '__main__':

    z = 10
    n = z
    m = z
    l = z

    A = np.random.randint(0, 10, size=(n, m))
    print(A, "\n")

    B = np.random.randint(0, 10, size=(m, l))
    print(B, "\n")

    t1_o = time.time()
    C = Mat_Mult_S(A, B)
    t1_f = time.time()
    print(t1_f - t1_o)
    print(C, "\n")

    t2_o = time.time()
    D = Mat_Mult_P(A, B, 2)
    t2_f = time.time()
    print(t2_f - t2_o)
    print(D, "\n")



