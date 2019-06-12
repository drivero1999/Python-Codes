#Manejo de Archivos
#Leer archivo por medio de una expresion regular, tener en cuenta las ","

from sys import stdin
import re
import csv


def Departamento():
    regularExpre=r"^(\d+)\,(.+)\,(\d+)\,(.+)\,(.+)\,(.+)\,(.+)\,(.+)\,(\d+)\,(.+)\,(\d+)\,(\d+)\,(\d+)\,(\d+)\,(\d+\.\d)\,(.+)"
    archivo = open("Cadena_Productiva_Cafe.csv", 'r')
    archivoW=open("Departamento.csv",'w')
    for entrada in archivo:
        expresion=re.search(regularExpre,entrada)
        if(expresion):
            COD_DEP,DEPARTAMENTO,COD_MUN,MUNICIPIO,GRUPO_CULTIVO,SUB_CULTIVO,CULTIVO,DESAGREGACION,COD_CULTIVO,NOMBRE,PERIODO,Area_Sembrada,Area_Cosechada,Produccion,Rendimiento,ESTADO=expresion.groups()
            if(int(COD_DEP)==54):
                archivoW.write(COD_DEP + " ")
                archivoW.write(DEPARTAMENTO + " ")
                archivoW.write(COD_MUN + " ")
                archivoW.write(MUNICIPIO + " ")
                archivoW.write(GRUPO_CULTIVO + " ")
                archivoW.write(SUB_CULTIVO + " ")
                archivoW.write(DESAGREGACION + " ")
                archivoW.write(COD_CULTIVO + " ")
                archivoW.write(NOMBRE + " ")
                archivoW.write(PERIODO + " ")
                archivoW.write(Area_Sembrada + " ")
                archivoW.write(Area_Cosechada + " ")
                archivoW.write(Produccion + " ")
                archivoW.write(Rendimiento + " ")
                archivoW.write(ESTADO + " ")
                archivoW.write("\n")


def produccionxMunicipio():
    regularExpre=r"^(\d+)\,(.+)\,(\d+)\,(.+)\,(.+)\,(.+)\,(.+)\,(.+)\,(\d+)\,(.+)\,(\d+)\,(\d+)\,(\d+)\,(\d+)\,(\d+\.\d)\,(.+)"
    archivo = open("Cadena_Productiva_Cafe.csv", 'r')
    for entrada in archivo:
        expresion=re.search(regularExpre,entrada)
        if(expresion):
            COD_DEP,DEPARTAMENTO,COD_MUN,MUNICIPIO,GRUPO_CULTIVO,SUB_CULTIVO,CULTIVO,DESAGREGACION,COD_CULTIVO,NOMBRE,PERIODO,Area_Sembrada,Area_Cosechada,Produccion,Rendimiento,ESTADO=expresion.groups()
            print(MUNICIPIO,Produccion)

def mayoresRendimientosxPeriodo():
    regularExpre=r"^(\d+)\,(.+)\,(\d+)\,(.+)\,(.+)\,(.+)\,(.+)\,(.+)\,(\d+)\,(.+)\,(\d+)\,(\d+)\,(\d+)\,(\d+)\,(\d+\.\d)\,(.+)"
    archivo = open("Cadena_Productiva_Cafe.csv", 'r')
    lista=[]
    for entrada in archivo:
        expresion=re.search(regularExpre,entrada)
        if(expresion):
            COD_DEP,DEPARTAMENTO,COD_MUN,MUNICIPIO,GRUPO_CULTIVO,SUB_CULTIVO,CULTIVO,DESAGREGACION,COD_CULTIVO,NOMBRE,PERIODO,Area_Sembrada,Area_Cosechada,Produccion,Rendimiento,ESTADO=expresion.groups()
            if(float(Rendimiento)*10<int(PERIODO)):
                lista.append(MUNICIPIO)
    lista2=lista[0:10]
    print(lista2)

            
def main():
  Departamento()
  produccionxMunicipio()
  mayoresRendimientosxPeriodo()
  

main()