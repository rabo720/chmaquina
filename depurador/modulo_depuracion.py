'''
Created on 27/02/2012

@author: Ricardo Andres Burgos Ocampo
'''


def buscar_variables(vec,variable):
    variable=variable.strip()
    for elemento in vec:
        if elemento[0] == variable:
            return True
    return False

            
def agregar_variable(vec_variables,linea):
    x=[linea[1],linea[3]]
    vec_variables.append(x)


def agregar_etiqueta(vec_etiquetas,linea):
    x=[linea[1],linea[2]]
    vec_etiquetas.append(x)

def casteo_variable(variable, tipo):
    if tipo == "I":
        variable=int(variable)
        return variable
    elif tipo == "R":
        variable=float(variable)
        return variable
    elif tipo == "C":
        variable=str(variable)
        return variable
    
def decc_pal_res(linea,vec_variables,vec_etiquetas,num_linea):
           
    Num_parametros=len(linea)
   
    lista=["cargue",
           "almacene",
           "lea",
           "sume",
           "reste",
           "multiplique",
           "divida",
           "potencia",
           "modulo",
           "concatene",
           "elimine",
           "extraiga",
           "muestre",
           "imprima",]
    
    tipo_variblea=["I","C","R"]
    
    def depuracion_basica():
        if Num_parametros==2:
            return buscar_variables(vec_variables,linea[1])
        return False

    def vaya():
        if Num_parametros==2:
            return buscar_variables(vec_etiquetas,linea[1])
        return False
        
    def vayasi():
        if Num_parametros==3:
            x = buscar_variables(vec_etiquetas,linea[1])
            y = buscar_variables(vec_etiquetas, linea[2])
            return x and y
        return False
        
    def nueva():
        if linea[2]in tipo_variblea:
            if Num_parametros==4:
                linea[3]=casteo_variable(linea[3].strip("\n"),linea[2])
                agregar_variable(vec_variables, linea)
                return True
            elif Num_parametros==3:
                linea.append(casteo_variable(0,linea[2]))
                agregar_variable(vec_variables, linea)
                return True
            else:
                return False
        else:
            return False
                    
    def etiqueta():
        if Num_parametros==3:
            try:
                linea[2]=int(linea[2])
                if num_linea > linea[2]:
                    agregar_etiqueta(vec_etiquetas,linea)
                    return True
                else:
                    return False
            except ValueError:
                return False    
        else:
            return False
    
    def retorne():
        if Num_parametros==2:
            if linea[1]=="0":
                return True
            else:
                return False
        else:
            return False
        
    def default():
        return False
    
        
    
    dicc_func={
               "depuracion_basica":depuracion_basica,
               "vaya":vaya,
               "vayasi":vayasi,
               "nueva":nueva,
               "etiqueta":etiqueta,
               "default":default,
               "retorne":retorne
               }    

    if linea[0] in lista:
        return dicc_func["depuracion_basica"]
    elif linea[0] in dicc_func:
        return dicc_func[linea[0]]
    else:
        return dicc_func["default"]
    
    
        
    
        