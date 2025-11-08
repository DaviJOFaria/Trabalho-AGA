import sys

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
    
print("=== Calculo de determinantes de matriz ===")

linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))

if(linhas != colunas):
    print("Matriz nao é quadrada, determinante invalida")
    sys.exit()

matriz = []
print("Digite o conteudo da matriz separado por espaços:")

for i in range(linhas):
    userLinha = input()
    # Divide a string e converte os elementos para inteiros
    matrizLinha = list(map(int, userLinha.split()))
    matriz.append(matrizLinha)

print("\nMatriz: ")
for matrizLinha in matriz:
    print(matrizLinha)

detMatriz = calculoDet(matriz)
print(detMatriz)
