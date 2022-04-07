# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

# Module
import os
from Generar_Informe import Informe
from tkinter import *

#Main Class
class Panel_Principal():
    def __init__(self):
        #Window configuration
        self.ventana = Tk()
        self.ventana.geometry('600x600')
        self.ventana.title('Empresas Scout')
        
        self.Ruta_Trabajo = os.getcwd()
        self.ventana.iconbitmap('{}\\Icons\\saludo_scout.ico'.format(self.Ruta_Trabajo))
        self.ventana.resizable(0, 0)
        self.ventana.config(bg='violet', cursor='tcross')
        self.Widgets()
        
    def Widgets(self):
        #Labels
        self.LbInforme = Label(text='Informe Scout')
        self.LbInforme.config(bg='violet', fg='black', font='Italic 16 bold', justify='center')
        self.LbInforme.place(x=200, y=70, width=200, height=40)
        
        self.LbNombre_Proyecto = Label(text='Nombre del proyecto / empresa:')
        self.LbNombre_Proyecto.config(bg='light green', fg='black', font='Normal 8', justify='center')
        self.LbNombre_Proyecto.place(x=20, y=200, width=180, height=40)
        
        self.LbPlata_Recaudada = Label(text='Plata total recaudada:')
        self.LbPlata_Recaudada.config(bg='light green', fg='black', font='Normal 8', justify='center')
        self.LbPlata_Recaudada.place(x=20, y=280, width=180, height=40)
        
        self.LbGastos = Label(text='Gastos:')
        self.LbGastos.config(bg='light green', fg='black', font='Normal 8', justify='center')
        self.LbGastos.place(x=20, y=360, width=180, height=40)
        
        self.LbNombre_Grupo = Label(text='Nombre del grupo scout:')
        self.LbNombre_Grupo.config(bg='light green', fg='black', font='Normal 8', justify='center')
        self.LbNombre_Grupo.place(x=20, y=440, width=180, height=40)
        
        
        #Entrys
        self.EnNombre_Proyecto = Entry()
        self.EnNombre_Proyecto.config(bg='white', fg='black', font='Normal 8', justify='left')
        self.EnNombre_Proyecto.place(x=220, y=200, width=350, height=40)
        
        self.EnPlata_Recaudada = Entry()
        self.EnPlata_Recaudada.config(bg='white', fg='black', font='Normal 8', justify='left')
        self.EnPlata_Recaudada.place(x=220, y=280, width=350, height=40)
        
        self.EnGastos = Entry()
        self.EnGastos.config(bg='white', fg='black', font='Normal 8', justify='left')
        self.EnGastos.place(x=220, y=360, width=350, height=40)
        
        self.EnGrupo = Entry()
        self.EnGrupo.config(bg='white', fg='black', font='Normal 8', justify='left')
        self.EnGrupo.place(x=220, y=440, width=350, height=40)
        
        
        #Button
        self.BtGenerar_Informe = Button(text='Generar Informe', command= lambda: self.Generador())
        self.BtGenerar_Informe.config(bg='light blue', fg='black', font='Normal 8 bold', justify='center')
        self.BtGenerar_Informe.place(x=220, y=500, width=100, height=40)
    
    
    def RunApp(self):
        self.ventana.mainloop()
        
    def Generador(self):
        self.Nombre_Proyecto = self.EnNombre_Proyecto.get()
        self.Plata_Recaudada = self.EnPlata_Recaudada.get()
        self.Gastos = self.EnGastos.get()
        self.Gastos = self.Gastos.split()
        self.Grupo = self.EnGrupo.get()
        
        Informe(self.Nombre_Proyecto, self.Plata_Recaudada, self.Gastos, self.Grupo)
        
    

if __name__ == '__main__':
    Sofware = Panel_Principal()
    Sofware.RunApp()
    