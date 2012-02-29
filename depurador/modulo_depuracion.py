'''
Created on 27/02/2012

@author: Ricardo Andres Burgos Ocampo
'''

def buscar_variables(vec_variables,variable):
    for elemento in vec_variables:
        if elemento[0] == variable:
            return True
    return False

            
def agregar_variable(vec_variables,variable,contenido):
    x=[variable,contenido]
    vec_variables.append(x)
    return vec_variables


    
def decc_pal_res(cadena,linea,vec_variables):
        
    def cargue():
        return buscar_variables(vec_variables,linea[1])
    def almacene():
        return buscar_variables(vec_variables,linea[1])
    def vaya():
        print "contenido"
        
    def vayasi():
        print "contenido"
        
    def nueva():
        Num_parametros=len(linea)
        if Num_parametros==4:
            agregar_variable(vec_variables, linea[1],linea[3])
            print vec_variables[0]
            return True
        elif Num_parametros==3:
            agregar_variable(vec_variables, linea[1],0)
            return True
        else:
            return False
                    
        
    
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
    
    
        
    
        