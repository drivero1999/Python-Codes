#Operaciones Con Vectores

import random
def crearVector(N,vInf,vSup):
  vector=[0]*N
  for i in range(N):
    vector[i]=random.randint(vInf,vSup)
  return vector

def sumarVector(vector1,vector2):
  tam=len(vector1)
  aux=[0]*tam
  for i in range(tam):
    aux[i]=vector1[i]+vector2[i]
  return aux

def ordena(vector,N):
  for i in range(len(vector)-1,0,-1):
    pos=0
    for j in range(1,i+1):
      if(vector[j]>vector[pos]):
        pos=j
        
    temp=vector[i]
    vector[i]=vector[pos]
    vector[pos]=temp
      
  aux=[]    
  band=[]
  for i in reversed(vector):
    band.append(i)
    
  for j in range(len(band)):
    if(j<N):
      aux.append(band[j])
    
  return aux

def main():
  print("Ingrese la dimension del vector: ")
  n=int(input())
  print("Ingrese el valor inferior : ")
  m=int(input())
  print("Ingrese el valor superior: ")
  k=int(input())
  vector1=crearVector(n,m,k)
  vector2=crearVector(n,m,k)
  print("Vector 1: ", vector1)
  print("Vector 2: ", vector2)
  vector3=sumarVector(vector1,vector2)
  print("La suma de los vectores es: ", vector3)
  print("Ingrese los N valores mayores: ")
  N=int(input())
  vector4=ordena(vector3,N)
  print("Los N valores mayores son : ", vector4)
  
main()