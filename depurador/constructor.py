'''
Created on 27/02/2012

@author: Ricardo Andres Burgos Ocampo
'''
"""
    Dentro del vec_variables se encuentra alojada una m, el archivo "algoritmo.txt" tiene un cargue m
    si se ejecuta el programa se vera como se realiza el manejo de esta linea.

"""
from procesador import procesador

if __name__ == '__main__':
    
    a="algoritmo.txt" #variable que aloja el archivo 
    f= open(a,"r")#se abre el archivo
    procesador_ob=procesador(f)
    procesador_ob.cargar_programa()
    
        