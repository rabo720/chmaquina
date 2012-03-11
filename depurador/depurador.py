'''
Created on 27/02/2012

@author: Ricardo Andres Burgos Ocampo
'''
from modulo_depuracion import decc_pal_res #modulo donde se encuentra el trato de cada una de las palabras reservadas


class depurador(object):
    #Constructor
    def __init__(self, File, vec_variables, vec_etiquetas):
        self.File = File
        self.vec_variables = vec_variables
        self.vec_etiquetas = vec_etiquetas
        
    """
    Revision_linea: Se revisa una linea, para conocer si no se encuntra con errores de sintaxis
    Entrada:
        cadena: En su interior se encuntra una linea de codigo que se extrajo del codigo a revisar
        vec_variables: El vector en donde se encuntran todas las variables
        vec_etiquetas: El vector end onde se encuntran todas las etiquetas
        contador: Se trata de el numero de lineas que trae todo el archivo a revisar
    Retorna: 
        BOOLEAN

    """    
    def revision_linea(self, cadena, vec_variables, vec_etiquetas, contador_pal):
        verificador = decc_pal_res(cadena, vec_variables, vec_etiquetas, contador_pal)()
        return verificador
    
    """
    contar_lineas: Cuenta la cantidad de lineas que trae el codigo en el archivo.
    Entradas:
        null
    Retorna:
        contador: Numero de lineas.

    """     
    def contar_lineas(self):
        contador=0
        while True:
            line = self.File.readline()
            contador+=1
            if not line:
                self.File.seek(0,0)
                return contador
            
    """
    iniciar_etiquetas: Se trata de la primera corrida de el codigo, en donde se crean todas las instancias de 
                        etiquetas del programa
    Entrada:
        null
    Retorna:
        BOOLEAN  
    """
                 
    def iniciar_etiquetas(self):
        contador = 0
        num_lineas=self.contar_lineas()
        while True:
            linea = self.File.readline()
            if not linea:
                return True
            linea = linea.split(" ")
            contador += 1
            if linea[0] == "etiqueta":
                    if self.revision_linea(linea, self.vec_variables, self.vec_etiquetas, num_lineas) == False:
                        print "se debe realizar una correccion en la line numero ", contador
                        return False
                
    """
    depuracion_lineas: Verifica que la sintanxis de todas las lineas de codigo sea la correcta.
    Entrada:
        null
    Retorna:
        BOOLEAN
    """                
          
    def depuracion_lineas(self):
        contador = 0
        while True:
            linea = self.File.readline()
            contador += 1
            if not linea:
                print "no se han encontrado errores de sintanxis"
                return True
            linea =linea.split(" ")
            if linea[0] != "etiqueta":
                if not linea[0].startswith("//") and not linea[0].startswith("\n"):
                    if self.revision_linea(linea, self.vec_variables, self.vec_etiquetas, contador) == False:
                        print "se debe realizar una correccion en la line numero ", contador
                        return False
    
    """
    manejo_archivo: Realiza la instancia de las etiquetas y de las varuiables, ademas se verifica que no se encuntren errores
                    de sinstanxis en todo el archivo con el codigo del programa
    Entrada:
        null
    Retorna:
        BOOLEAN
    """            
    
    def manejo_archivo(self):
        if self.iniciar_etiquetas():
            self.File.seek(0,0)
            self.depuracion_lineas()
            self.File.seek(0,0)
            return True
   
    
        
