'''
Created on 27/02/2012

@author: Ricardo Andres Burgos Ocampo
'''
import modulo_depuracion #modulo donde se encuentra el trato de cada una de las palabras reservadas

class depurador(object):
   
    #Constructor
    def __init__(self,File):
        self.File=File
    
    """
    Revision linea por linea si se encuentra bien realizada y si se usa una variable existente
    Entran:
        linea: Se trata de una de las lineas de codigo que se va a revisar
        vec_variable: es el vector en donde se encontraran todas las variables que han sido inicializadas
    Retorna: Boolean

    """  
    def revision_linea(self,linea,vec_variables):
        cadena=linea.split(" ")
        verificador=modulo_depuracion.decc_pal_res(cadena[0], cadena,vec_variables)()
        return verificador
    
    """
    Se abre el archivo y se le entrega a la funcion revision_linea cada una de las lineas 
    de codigo que esten dentro del documento

    """               
    def manejo_archivo(self):
        f= open(self.File,"r")
        contador=0
        vec_variables=["m"]
        while True:
            linea=f.readline()
            contador+=1
            if not linea:
                print "no se han encontrado errores de sintanxis"
                break
            if self.revision_linea(linea,vec_variables)==False:
                print "se debe realizar una correccion en la line numero ", contador
                break
        
   
    
        
