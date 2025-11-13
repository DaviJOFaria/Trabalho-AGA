import numpy as np
import time

def determinante_gaussiana(A):
    A = A.astype(float)
    n = A.shape[0]
    det = 1.0
    num_trocas = 0
    
    for i in range(n):
        pivo_idx = np.argmax(np.abs(A[i:, i])) + i
        
        if A[pivo_idx, i] == 0:
            return 0.0 
        
        if pivo_idx != i:
            A[[i, pivo_idx]] = A[[pivo_idx, i]]
            num_trocas += 1
            
        for j in range(i + 1, n):
            fator = A[j, i] / A[i, i]
            A[j, i:] -= fator * A[i, i:]
            
    for i in range(n):
        det *= A[i, i]
        
    if num_trocas % 2 == 1:
        det *= -1
        
    return det

#Exemplo
matriz_grande = np.array([
[1, 4, 7, 2, 9, 5, 3, 8, 6, 10],
[5, 9, 2, 8, 1, 6, 4, 7, 3, 11],
[3, 6, 8, 4, 7, 2, 9, 1, 5, 12],
[9, 1, 5, 3, 6, 8, 7, 2, 4, 13],
[7, 3, 6, 9, 2, 1, 8, 5, 10, 14],
[4, 8, 1, 6, 5, 9, 2, 3, 7, 15],
[6, 2, 9, 1, 8, 4, 5, 10, 11, 16],
[8, 5, 3, 7, 4, 10, 1, 6, 9, 17],
[2, 7, 4, 5, 3, 11, 6, 9, 8, 18],
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
])

inicio = time.time()
det_calculado = determinante_gaussiana(matriz_grande)
fim = time.time()

print(f"=== Cálculo do Determinante por Eliminação Gaussiana ===")
print(f"\nMatriz:\n{matriz_grande}")
print(f"\nDeterminante Calculado: {det_calculado:.2f}")
print(f"Tempo:{(fim-inicio):.9f}s")

#Numpy
#det_numpy = np.linalg.det(matriz_grande)
#print(f"Verificação (NumPy): {det_numpy:.2f}")