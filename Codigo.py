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
        listasumaprecio=[]

        if opcion==1:
            ciclo=1
            print(separador+"Bienvenido al registrador de ventas"+separador)
            while ciclo==1:
                listadescript=[]
                listacantidadt=[]
                listapreciot=[]
                listatiempot=[]
                
                print(f"VENTA {contador}")
                contadorventa.append(f"Venta{contador}")
                
                descripcion=input("Dime la descripcion del articulo : ")
                listadescript.append(descripcion)
                
                cantidad=int(input("Dime la cantidad de piezas vendidas : "))
                listacantidadt.append(cantidad)
                
                precio=float(input("Dime el precio de venta unitario : "))
                listasumaprecio.append(precio*cantidad)
                listapreciot.append(precio)
            
                ahora = datetime.datetime.now()
                ahora1=ahora.strftime('%d/%m/%Y')
                listatiempot.append(str(ahora1))
                
                diccionariov["Descripcion"]=listadescript
                diccionariov["Piezas"]=listacantidadt
                diccionariov["Precio"]=listapreciot
                diccionariov["Tiempo"]=listatiempot
                diccionario2=pd.DataFrame(diccionariov)
                #diccionario2.index=contadorventa
              
                ruta = "ventas.csv"
                diccionario2.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
            
                contador=contador+1            
                print(separador)
                print("Ingresa el numero 1 si deseas seguir registrando ventas\nIngresa el numero 0 si deseas salir del registrador de ventas")
                ciclo=int(input(":"))
                print(separador)
                print("")
                
            
            print(separador)
            print(f"Este es el monto total a pagar : {sum(listasumaprecio)}")
            print(separador)