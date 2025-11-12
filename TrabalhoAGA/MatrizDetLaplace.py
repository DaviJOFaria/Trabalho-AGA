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
        
print("=== Calculo de determinantes de matriz ===")

ordem = int(input("Digite a ordem da matriz: "))

matriz = []
print("Digite o conteudo da matriz separado por espaços:")

for i in range(ordem):
    userLinha = input()
    # Divide a string e converte os elementos para inteiros
    matrizLinha = list(map(int, userLinha.split()))
    matriz.append(matrizLinha)

print("\nMatriz: ")
for matrizLinha in matriz:
    print(matrizLinha)

detMatriz = calculoDet(matriz)
print(f"Determinante = {detMatriz}")

if( detMatriz == 0 ):
    print("Matriz singular. Não possui inversa")

else:
    print("Matriz não singular. Invertível")