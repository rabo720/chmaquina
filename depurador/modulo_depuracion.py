'''
Created on 27/02/2012

@author: Rabo
'''

    
    
def decc_pal_res(cadena,linea):
        
    def cargue():
        print "contenido"
        return True
    
    def almacene():
        
        print "contenido"
        
    def vaya():
        print "contenido"
        
    def vayasi():
        print "contenido"
        
    def nueva():
        print "contenido"
    
    def etiqueta():
        print "contenido"
    
    def lea():
        print "contenido"
    
    def sume():
        print "contenido"
    
    def reste():
        print "contenido"
    
    def multiplique():
        print "contenido"
    
    def divida():
        print "contenido"
    
    def potencia():
        print "contenido"
    
    def modulo():
        print "contenido"
    
    def concatene():
        print "contenido"
    
    def elimine():
        print "contenido"
    
    def extraiga():
        print "contenido"
    
    def muestre():
        print "contenido"
    
    def imprima():
        print "contenido"
    
    def retorne():
        print "contenido"
        
    def default():
        return False    
    """
    dicc_fun: es un dicccionario que contiene una 
    referencia de las palabras reservadas con las funciones
    que corresponde a cada una de ellas. 
    """
    dicc_func={
               "cargue":cargue,
               "almacene":almacene,
               "vaya":vaya,
               "vayasi":vayasi,
               "nueva":nueva,
               "etiqueta":etiqueta,
               "lea":lea,
               "sume":sume,
               "reste":reste,
               "multiplique":multiplique,
               "divida":divida,
               "potencia":potencia,
               "modulo":modulo,
               "concatene":concatene,
               "elimine":elimine,
               "extraiga":extraiga,
               "muestre":muestre,
               "imprima":imprima,
               "retorne":retorne,
               "default":default
                }
    
    if dicc_func.has_key(cadena)==True:
        return dicc_func[cadena]
    else:
        return dicc_func["default"]
    
    
        
    
        