import datetime
import sys
import pandas as pd
import csv
import os

menu=1
separador=("*"*30)
contador=1
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
            

            
            
            
        elif opcion==2:
            try:
                contador=1
                contador1=0
                contador2=0
                print(separador+"Bienvenido al consultador de ventas"+separador)
                print("-"*20)
                dia=(input("Dime el dia en el que registraste la venta : "))
                mes=input("Dime el mes en el que registraste la venta : ")
                año=input("Dime el año en el que registraste la venta : ")
                
                if len(mes)==1:
                    mes=("0"+ mes)
                    
                if len(dia)==1:
                    dia2=("0"+dia+"/")
                    fecha=(dia2+mes+"/"+año)
                else:
                    fecha=(dia+"/"+mes+"/"+año)
                print("")
                
                
                
                with open ('ventas.csv') as file:
                    reader=csv.reader(file)
                    for registro in reader:
                        contador1=contador1+1
                        if registro[-1]==fecha:
                            print("*"*10 + f"VENTA {contador}" + "*"*10)
                            print(f"Descripcion:{registro[0]}" )
                            print(f"Piezas:{registro[1]}" )
                            print(f"Precio:{registro[2]}" )
                            print(f"Tiempo:{registro[3]}" )
                            print(separador)
                            contador=contador+1
                        
                        elif registro[-1]!=fecha:
                            contador2=contador2+1
                            
                    if contador2==contador1:
                        print(f"No hay registros de ventas con esta fecha :( {fecha} ")
               
            except:
                print("No se han registrado ventas")
        
        
        elif opcion==3:
            break
        
            
           
                
            
        
except:
    print(f"Ocurrió un problema {sys.exc_info()[0]}")

finally:
    print("FIN DEL CODIGO")  