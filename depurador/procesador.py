'''
Created on 10/03/2012

@author: Rabo
'''
from depurador import depurador
from memoria import memoria


"""vec_variables=[]#inicializacion del vector para las variables
    vec_etiquetas=[]#inicializacion del vector para las etiquetas
    vec_programas=[]#Inicializacion del vector para las posicionesde los programas
    a="algoritmo.txt" #variable que aloja el archivo 
    
    me=memoria(40,200)# me.inicializar_Acm()
    f= open(a,"r")#se abre el archivo
    
    b=depurador(f,vec_variables,vec_etiquetas)#creacion de objeto
    #llamdo de un metodo del objeto
    if b.manejo_archivo(): 
        me.get_cargar_programa(f,vec_variables, vec_programas)"""
        



class procesador(object):
    #atributos
    vec_variables=[]#inicializacion del vector para las variables
    vec_etiquetas=[]#inicializacion del vector para las etiquetas
    vec_programas=[]#Inicializacion del vector para las posicionesde los programas   

    def __init__(self,file):
        self.file=file
        
    def cargar_programa(self):
        depurador_ob=depurador(self.file,self.vec_variables,self.vec_etiquetas)
        memoria_ob=memoria(40,200)
        if depurador_ob.manejo_archivo():
            memoria_ob.get_cargar_programa(self.file, self.vec_variables, self.vec_programas)
            
        
        