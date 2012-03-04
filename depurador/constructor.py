'''
Created on 27/02/2012

@author: Ricardo Andres Burgos Ocampo
'''
"""
    Dentro del vec_variables se encuentra alojada una m, el archivo "algoritmo.txt" tiene un cargue m
    si se ejecuta el programa se vera como se realiza el manejo de esta linea.

"""
import depurador

if __name__ == '__main__':
    
    vec_variables=[]
    vec_etiquetas=[]
    a="algoritmo.txt" #variable que aloja el archivo 
    f= open(a,"r")
    b=depurador.depurador(f,vec_variables,vec_etiquetas)#creacion de objeto
    b.manejo_archivo()#llamdo de un metodo del objeto
    
    
    