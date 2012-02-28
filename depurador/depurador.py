'''
Created on 27/02/2012

@author: Rabo
'''
import modulo_depuracion


class depurador(object):
   
    def __init__(self,File):
        self.File=File
        
    def revision_linea(self,linea):
        cadena=linea.split(" ")
        verificador=modulo_depuracion.decc_pal_res(cadena[0], cadena)()
        return verificador
                   
    def manejo_archivo(self):
        f= open(self.File,"r")
        contador=0
        while True:
            linea=f.readline()
            contador+=1
            if not linea:
                print "no se han encontrado errores de sintanxis"
                break
            if self.revision_linea(linea)==False:
                print "se debe realizar una correccion en la line numero ", contador
                break
        
   
    
        
