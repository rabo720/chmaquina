'''
Created on 6/03/2012

@author: Ricardo Andres Burgos 
'''

class memoria(object):
    
    mem=[]
        
    def __init__(self,tam_OS, tam_ve ):
        self.tam_OS = tam_OS
        self.pc=tam_OS
        self.vec=tam_ve
        self.iniciar()

    def iniciar_memoria(self):
        x=0
        while self.vec > x:
            self.mem.append("Espacio libre")
            x+=1  
    def inicializar_OS(self):
        x=1
        while self.tam_OS>x:
            self.mem[x]="Sistema operativo"
            x+=1
    
    def iniciar(self):
        self.iniciar_memoria()
        self.inicializar_OS()
        self.inicializar_Acm()
        
    def inicializar_Acm(self):
        self.mem[0]=0
        
    def get_cargar_lineas(self,Archivo):
        
        while True:
            linea = Archivo.readline()
            if not linea:
                break
            self.mem[self.pc]= linea
            self.pc+=1
            
    def get_cargar_variables(self, vec_variables):
        x=0
        num_var=len(vec_variables)
        while True:
            self.mem[self.pc]=vec_variables[x][1]
            vec_variables[x][1]=self.pc
            self.pc+=1
            x+=1
            if x==num_var:
                break
    
    def get_cargar_programa(self, Archivo, vec_variables, vec_programa):
        self.pc=self.tam_OS
        Inicio_programa=self.pc
        self.get_cargar_lineas(Archivo)
        Fin_programa=self.pc
        self.get_cargar_variables(vec_variables)
        Fin_total=self.pc
        programa=[Inicio_programa,Fin_programa,Fin_total]
        vec_programa.append(programa)
    
    
              
        