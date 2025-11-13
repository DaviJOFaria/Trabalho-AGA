import time

def laplace(matriz, xLinha, xColuna):
    newMatriz = []

    for i, linha in enumerate(matriz):
        if i != xLinha:
            newLinha = []
            for j, num in enumerate(linha):
                if j != xColuna:
                    newLinha.append(num)
            if newLinha:
                newMatriz.append(newLinha)
    return newMatriz

def calculoDet(matriz):
    ordem = len(matriz)


    if ( ordem == 1 ):
        return matriz[0][0]
    
    if ( ordem == 2 ):
        return (matriz[0][0] * matriz [1][1]) - (matriz[0][1] * matriz[1][0])
    
    if ( ordem == 3 ):
        return (((matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0])
        + (matriz[0][2] * matriz[1][0] * matriz[2][1] )) - ((matriz[0][1] * matriz [1][0] * matriz[2][2]) + 
        (matriz[0][0] * matriz[1][2] * matriz [2][1]) + (matriz[0][2] * matriz[1][1] * matriz[2][0])))
    
    det = 0
    
    for j in range(ordem):
        sinalCofator = (-1) ** j
        submatriz = laplace(matriz, 0, j)
        detSubmatriz = calculoDet(submatriz)

        det += matriz[0][j] * sinalCofator * detSubmatriz
    
    return det
        
print("=== Cálculo do Determinante por Teorema de Laplace ===")

'''ordem = int(input("Digite a ordem da matriz: "))

matriz = []
print("Digite o conteudo da matriz separado por espaços:")

for i in range(ordem):
    userLinha = input()
    # Divide a string e converte os elementos para inteiros
    matrizLinha = list(map(int, userLinha.split()))
    matriz.append(matrizLinha) '''

matriz =([
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

print("\nMatriz: ")
for matrizLinha in matriz:
    print(matrizLinha)

inicio = time.time()
detMatriz = calculoDet(matriz)
fim = time.time()

total = fim - inicio

print(f"Determinante = {detMatriz}")
print(f"Tempo:{total:.9f}s")