import numpy as np
from scipy.linalg import lu

def soltrsup(A, b):
    if np.linalg.det(A) == 0:
        print('La matriz es singular')
        return []

    n = A.shape[0]
    x = b

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            x[i] = b[i] - A[i, j] * x[j]
        
        x[i] = x[i] / A[i, i]
    
    return x


def soltrinf(A,b):

	if np.linalg.det(A) == 0:
		print('La matriz es singular')
		return None

	n = A.shape[0]
	x = b     						
	
	for i in range(n):
		for j in range(i): 			
			x[i] = b[i] - A[i,j] * x[j]

		x[i] = x[i]/A[i,i]

	return x

def sollu(A_, b_):
    A = np.copy(A_)
    b = np.copy(b_)
    P, L, U = lu(A)
    sol_tr_inf = soltrinf(L, np.transpose(P) @ b) 
    sol_tr_sup = soltrsup(U, sol_tr_inf)

    return sol_tr_sup