import datetime
import sys
import pandas as pd
import csv
import os

menu=1
separador=("*"*30)
contador=1
contadorventa=[]
diccionariov={}
try:
    while menu==1:
        print(separador+"Bienvenido al Menu Principal" +separador)
        print("Opciones del menu")
        print("1=Registrar una Venta\n2=Consultar ventas de un día específico\n3=Salir")
        opcion=int(input("Que opcion eliges : "))