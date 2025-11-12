import numpy as np

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
    [1, 5, 2, 8, 4],
    [3, 0, 7, 1, 9],
    [6, 4, 1, 2, 5],
    [9, 2, 3, 7, 0],
    [0, 1, 8, 6, 3]
])

det_calculado = determinante_gaussiana(matriz_grande)

print(f"--- Cálculo do Determinante por Eliminação Gaussiana ---")
print(f"Matriz de Entrada (5x5):\n{matriz_grande}")
print(f"\nDeterminante Calculado: {det_calculado:.2f}")

# Para referência e comparação (usando a função nativa do NumPy)
det_numpy = np.linalg.det(matriz_grande)
print(f"Verificação (NumPy): {det_numpy:.2f}")