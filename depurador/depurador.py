'''
Created on 27/02/2012

@author: Ricardo Andres Burgos Ocampo
'''
import modulo_depuracion #modulo donde se encuentra el trato de cada una de las palabras reservadas


class depurador(object):
    #Constructor
    def __init__(self, File, vec_variables, vec_etiquetas):
        self.File = File
        self.vec_variables = vec_variables
        self.vec_etiquetas = vec_etiquetas
        
    
    """
    Revision linea por linea si se encuentra bien realizada y si se usa una variable existente
    Entran:
        linea: Se trata de una de las lineas de codigo que se va a revisar
        vec_variable: es el vector en donde se encontraran todas las variables que han sido inicializadas
    Retorna: Boolean

    """   
        
    def revision_linea(self, cadena, vec_variables, vec_etiquetas, contador):
        verificador = modulo_depuracion.decc_pal_res(cadena, vec_variables, vec_etiquetas, contador)()
        return verificador
    
    """
    Se abre el archivo y se le entrega a la funcion revision_linea cada una de las lineas 
    de codigo que esten dentro del documento verificando si es una varaible o una etiqueta y las inicializa

    """             
    def contar_lineas(self):
        contador=0
        while True:
            line = self.File.readline()
            contador+=1
            if not line:
                self.File.seek(0,0)
                return contador
            
                          
    def iniciar_variables_y_etiquetas(self):
        contador = 0
        a=self.contar_lineas()
        while True:
            linea = self.File.readline()
            if not linea:
                return True
            linea = linea.split(" ")
            contador += 1
            if linea[0] == "etiqueta" or linea[0] == "nueva":
                if self.revision_linea(linea, self.vec_variables, self.vec_etiquetas, a) == False:
                    print "se debe realizar una correccion en la line numero ", contador
                    return False
                
                
    def depuracion_lineas(self):
        contador = 0
        while True:
            linea = self.File.readline()
            contador += 1
            if not linea:
                print "no se han encontrado errores de sintanxis"
                return True
            linea =linea.split(" ")
            if linea[0] != "etiqueta" and linea[0] != "nueva":
                if self.revision_linea(linea, self.vec_variables, self.vec_etiquetas, contador) == False:
                    print "se debe realizar una correccion en la line numero ", contador
                    return False
                
    
    def manejo_archivo(self):
        if self.iniciar_variables_y_etiquetas():
            self.File.seek(0,0)
            self.depuracion_lineas()
        
   
    
        
