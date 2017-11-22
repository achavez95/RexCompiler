from rexparse import *
from ply import *
import rexlex
from cubo import *
from stack import *
from cuadruplo import *
from variable import *
from function import *
import sys
import tkinter as tk
from tkinter import *
#Indica el cuadruplo a ejecutar
cuaditer = 0
#Pila de control para llamadas anidadas
controlstack = Stack()

#Clase de activation record que permite manejar el arbol de activacion
class ActivationRecord:
    def __init__(self,id, actualpara, returnvalue, localdata, temps, calledby):
        self.id = id
        self.actualpara = actualpara
        self.returnvalue = returnvalue
        self.localdata = localdata
        self.temps = temps
        self.calledby = calledby
    #Imprime todos los atributos
    def printAll (self):
        print ("ACTIVATION RECORD: %s" %self.id)
        print ("PARAMVALUES")
        for i in self.actualpara:
            print (i)
            print ("\n")
        print ("RETURNS: %s" %self.returnvalue)
        print ("LOCAL VARS")
        for v in self.localdata:
            print (v)
            print("\n")
        print ("TEMPORALS")
        print (self.temps.items())

#Variable que indica el Activation Record actual
currentActRec = None

def suma(a, b, dir):
    print(listavar)
    print("SUMA")
    res = memoria.value(a) + memoria.value(b)
    memoria.updateVar(dir, res)

def resta(a, b, dir):
    res = memoria.value(a) - memoria.value(b)
    memoria.updateVar(dir, res)

def mult(a, b, dir):
    res = memoria.value(a) * memoria.value(b)
    memoria.updateVar(dir, res)

def div(a, b, dir):
    res = memoria.value(a) / memoria.value(b)
    memoria.updateVar(dir, res)

def modulo(a, b, dir):
    res = memoria.value(a) % memoria.value(b)
    memoria.updateVar(dir, res)

def potencia(a, b, dir):
    res = pow(memoria.value(a), memoria.value(b))
    memoria.updateVar(dir, res)

def menorque(a, b, dir):
    res = memoria.value(a) < memoria.value(b)
    memoria.updateVar(dir, res)

def menorigual(a, b, dir):
    res = memoria.value(a) <= memoria.value(b)
    memoria.updateVar(dir, res)

def mayorque(a, b, dir):
    res = memoria.value(a) > memoria.value(b)
    print("RES:", res)
    memoria.updateVar(dir, res)

def mayorigual(a, b, dir):
    res = memoria.value(a) >= memoria.value(b)
    memoria.updateVar(dir, res)

def diferente(a, b, dir):
    res = memoria.value(a) != memoria.value(b)
    memoria.updateVar(dir, res)

def igual(a, b, dir):
    res = memoria.value(a) == memoria.value(b)
    memoria.updateVar(dir, res)

def andop(a, b, dir):
    res = memoria.value(a) and memoria.value(b)
    memoria.updateVar(dir, res)

def orop(a, b, dir):
    res = memoria.value(a) or memoria.value(b)
    memoria.updateVar(dir, res)

def notop(a, b, dir):
    res = not memoria.value(a)
    memoria.updateVar(dir, res)

def goto (a, b, dir):
    global cuaditer
    cuaditer = dir - 1
    print ("CUADITER", cuaditer)

def gotot (a, b, dir):
    if memoria.value(a):
        global cuaditer
        cuaditer = dir - 1

def gotof (a, b, dir):
    if not memoria.value(a):
        global cuaditer
        cuaditer = dir - 1

def assign (a, b, dir):
    memoria.updateVar(dir, memoria.value(a))
#Pila que guarda en donde se quedo la ejecucion antes de una llamada
pagemark = Stack()

def call (a, b, dir):
    global cuaditer
    pagemark.push(cuaditer)
    cuaditer = dir - 1
    controlstack.push(currentActRec)
    print("STACKL:", controlstack.size())

def returnop (a, b, dir):
    global currentActRec
    currentActRec.returnvalue = memoria.value(dir)
    print("CARECVAL: ", currentActRec.returnvalue)
    value = memoria.value(dir)
    for f in listafunc:
        if currentActRec.id == f.id:
            memoria.updateVar(f.rtn, value)    

def printop (a, b, dir):
    print("OUT: ",memoria.value(dir))

def param (a, b, dir):
    global currentActRec
    currentActRec.actualpara.append(memoria.value(a))
    memoria.updateVar(dir, memoria.value(a))

def assigncell (a, b, dir):
    memoria.updateVar(memoria.value(dir), memoria.value(a))

def endfunc (a, b, dir):
    #endfuncAR = control.pop()
    global cuaditer
    global currentActRec
    currentActRec.temps = memoria.getTemps()
    print("ACTUALPARA: ", currentActRec.actualpara[0])
    currentActRec.printAll()
    
    if pagemark:
        cuaditer = pagemark.pop()

def era (a, b, dir):
    funcion = listafunc[a-1]
    global currentActRec
    savedActRec = controlstack.pop()
    savedActRec.temps = memoria.getTemps()
    for f in listafunc:
        if f.id == savedActRec.id:
            savedActRec.localdata = f.parameters
            controlstack.push(savedActRec)
    paramlist = []
    currentActRec = ActivationRecord(funcion.id, paramlist, None,
                                     funcion.parameters, None, currentActRec.id)
    print("ERA:", currentActRec.id, currentActRec.localdata)

def inputop (a, b, dir):
    inputvar = input("INPUT: ")
    print(inputvar)
    memoria.updateVar(dir, inputvar)
    
#Valores para el switch
operations = {0: suma,
              1: resta,
              2: mult,
              3: div,
              4: modulo,
              5: potencia,
              6: menorque,
              7: menorigual,
              8: mayorque,
              9: mayorigual,
              10: diferente,
              11: igual,
              12: andop,
              13: orop,
              14: notop,
              15: goto,
              16: gotot,
              17: gotof,
              18: assign,
              19: call,
              20: returnop,
              21: printop,
              22: param,
              23: assigncell,
              24: endfunc,
              25: era,
              26: inputop}
#Creacion de ventana principal
class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.buttonvar = tk.Button(self, text="Variables", 
                                command=self.create_window_vars)
        self.buttonfunction = tk.Button(self, text="Function", 
                                command=self.create_window_func)
        self.buttoncondition = tk.Button(self, text="Condition", 
                                command=self.create_window_condition)
        self.buttonvar.pack(side="top")
        self.buttonfunction.pack()
        self.buttoncondition.pack()
    #Ventana para crear bloques
    def create_window_block(self):
        t = tk.Toplevel(self)
        Button(t, text='Variable', command=self.create_window_vars).grid(row = 0)
        Button(t, text='Condition', command=self.create_window_condition).grid(row = 1)
        Button(t, text='While', command=self.save_var).grid(row = 2)
        Button(t, text='Do', command=self.create_window_param).grid(row = 3)
    #Ventana para crear funciones
    def create_window_func(self):
        t = tk.Toplevel(self)
        tipo = StringVar(t)
        tipo.set("int")
        t.wm_title("Add function")
        Label(t, text="Type: ").grid(row=0)
        Label(t, text="ID: ").grid(row=0, column = 2)
        e1 = OptionMenu(t, tipo, "int", "dec", "fracc", "string", "bool")
        e2 = Entry(t)
        e1.grid(row=0, column = 1)
        e2.grid(row=0, column = 3)
        Button(t, text='Save', command=self.save_var).grid(row = 2, column = 0)
        Button(t, text='Parameter', command=self.create_window_param).grid(row = 2, column = 1)
        Button(t, text='Block', command=self.create_window_block).grid(row = 2, column = 2)
    #Ventana para crear parametros
    def create_window_param(self):
        t = tk.Toplevel(self)
        t.wm_title("Add parameter")
        Label(t, text="Type: ").grid(row=0)
        Label(t, text="ID: ").grid(row=0, column = 2)
        e1 = Entry(t)
        e2 = Entry(t)
        e1.grid(row=0, column = 1)
        e2.grid(row=0, column = 3)
        Button(t, text='Save', command=self.save_var).grid(row = 2, column = 1)
    #Ventana para crear variables
    def create_window_vars(self):
        t = tk.Toplevel(self)
        tipo = StringVar(t)
        tipo.set("int")
        t.wm_title("Add variables")
        Label(t, text="Type: ").grid(row=0)
        Label(t, text="ID: ").grid(row=0, column = 2)
        e1 = OptionMenu(t, tipo, "int", "dec", "fracc", "string", "bool")
        e2 = Entry(t)
        e1.grid(row=0, column = 1)
        e2.grid(row=0, column = 3)
        Button(t, text='Save', command=self.save_var).grid(row = 2)
    #Ventana para crear condiciones
    def create_window_condition(self):
        t = tk.Toplevel(self)
        t.wm_title("Add condition")
        Label(t, text="If: ").grid(row=0)
        e1 = Entry(t)
        e1.grid(row=0, column = 1)
        Button(t, text='Save', command=self.save_var).grid(row = 2, column = 1)
        Button(t, text='Block', command=self.create_window_block).grid(row = 2, column = 0)
    #Accion de boton save
    def save_var(self):
        print ("SAVED")
              
#Funcion para ejecutar un programa escogido
def runProgram():
    global cuaditer
    global currentActRec
    for f in listafunc:
        #Inserta el primer ActivationRecord de main
        if f.id == "main":
            paralist = []
            currentActRec = ActivationRecord(f.id, paralist, None, f.parameters, None, None)
            controlstack.push(currentActRec)
            break
    pagemark.push(len(cuadruplos))
    while cuaditer < len(cuadruplos):
        c = cuadruplos[cuaditer]
        print('[',cuaditer,']',cuadruplos[cuaditer])
        operations[c.pos1](c.pos2, c.pos3, c.pos4)
        
        cuaditer += 1
        print("PROGCUAD: ", cuaditer)
        memoria.printVars()
        
#Funcion que pregunta por el archivo y ejecuta runProgram una vez parseado el archivo
def OpenRunFile():
    file_path = filedialog.askopenfilename()
    f = open(file_path,"r")
    data = f.read()
    t = yacc.parse(data)
    print (pilao)
    print (ptipos)
    print (len(cuadruplos))
    memoria.printVars()
    for x in range (0, len(cuadruplos)) :
        print ('[',x,']',cuadruplos[x].pos1, ',' , cuadruplos[x].pos2,
            ',' ,cuadruplos[x].pos3, ',', cuadruplos[x].pos4)
    runProgram()
    reinitializeParser()
    global cuaditer
    cuaditer = 0

if __name__ == "__main__":
    root = tk.Tk()
    # Crear el toolbar
    menu = Menu(root)
    
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open and run", command=OpenRunFile)
    filemenu.add_command(label="Quit!", command=root.quit)

# Desplegar toolbar
    root.config(menu=menu)
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()



