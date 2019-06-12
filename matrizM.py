#Crear Matriz de la forma M

def crearMatrizM(digito,numFilas,numColum):
    matriz=[]
    for i in range(numFilas):
      a=[0]*numColum
      matriz.append(a)
    
    if(numColum%2==0):
        #print("Par")
        for i in range(numFilas):
            for j in range(numColum):
                matriz[0][j]=digito
                matriz[i][0]=digito
                matriz[i][-1]=digito
        for i in range(0,int((numFilas/2)+1)):
            matriz[i][int(numColum/2)]=digito
            matriz[i][int((numColum/2)-1)]=digito
    
    if(numColum%2!=0):
        #print("Impar")
        for i in range(numFilas):
            for j in range(numColum):
                matriz[0][j]=digito
                matriz[i][0]=digito
                matriz[i][-1]=digito
        for i in range(0,int((numFilas/2)+1)):
            matriz[i][int(numColum/2)]=digito

    return matriz

def imprimirMatriz(M):
    for i in M:
        print(i)

def main():
    print("Primer ejercicio, matriz M")
    n = int(input('Ingrese el numero de filas : '))
    m = int(input('Ingrese el numero de columnas : '))
    c = int(input('Ingrese el digito : '))
    M=crearMatrizM(c,n,m)
    imprimirMatriz(M)
    
main()
  