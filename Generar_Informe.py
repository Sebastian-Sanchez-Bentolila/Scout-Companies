# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

# Module
from openpyxl import Workbook
import os
import matplotlib.pyplot as plt
import socket
import shutil

def Informe(Proyecto: str, Recaudado: float, Gastos: list, Grupo: str):
    #Save Report to a folder on the desktop
    ruta_trabajo = os.getcwd()
    hostname = socket.gethostname()
    nueva_ruta_trabajo = str(f'C:\\Users\\{hostname}\\OneDrive\\Escritorio\\{Proyecto}')
    os.mkdir(f'{nueva_ruta_trabajo}')
    
    #Excel report
    wb = Workbook()
    hoja = wb.active
    
    #Scout group name
    hoja['A1'] = 'GRUPO:'
    hoja['B1'] = '{}'.format(Grupo)
    
    #Money raised
    hoja['F4'] = 'Recaudado'
    hoja['F5'] = float('{}'.format(Recaudado))
    
    #Expenses
    hoja['B4'] = 'Gastos'  
    i = 5
    Gasto_Total = 0
    for cont in Gastos:
        hoja[f'B{i}'] = float(f'{cont}')
        Gasto_Total = Gasto_Total + float(cont)
        i=i+1
    
    #Total expenses 
    hoja[f'B{i+1}'] = f'=SUM(B5:B{i})'
    
    #Profits
    hoja['F7'] = 'Ganancias'
    hoja['F8'] = f'=F5-B{i+1}'
    
    #Saved excel
    nombre_excel = str(f'{Proyecto}_INFORME.xlsx')
    wb.save(str(f'{nombre_excel}'))
    shutil.move(f'{ruta_trabajo}\\{nombre_excel}', f'{nueva_ruta_trabajo}\\{nombre_excel}')
    
    
    #Graphics
    ganancia = float(Recaudado) - Gasto_Total
    
    if ganancia>=0:
        
        grafico = [Gasto_Total, ganancia]
        etiqueta = ['Gasto Total', 'Ganancias']
        plt.pie(grafico, labels=etiqueta, autopct="%1.2f%%")
        plt.axis('equal')
        plt.title(f'{Proyecto}')
        nombre_torta = 'Gràfico_Tortas_Gastos'
        plt.savefig(nombre_torta)
        
        #Saved Graphics
        shutil.move(f'{ruta_trabajo}\\{nombre_torta}.png', f'{nueva_ruta_trabajo}\\{nombre_torta}.png') 