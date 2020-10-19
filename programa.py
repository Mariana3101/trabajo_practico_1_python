import funciones
import math
import os


def carga_datos():
	
	listado = []
	
	salir =""
	
	
	while salir != "si":
		
		# Aca se hace una excepcion para que cuando se ingrese un Numero en lugar de un string el programa continue y no se rompa 
		
		try:	
			# Se declara un diccionario vacio
			participante = {}
			participante["numero"]= int(input("Ingrese el numero del participante: "))
			participante["nombre"] = input("Ingrese el nombre: ")
					
			
			participante["apellido"] = input("Ingrese el apellido : ")
			participante["edad"] = int(input("Ingrese la edad: "))
			
		
			
			participante["sexo"] = input("Ingrese el sexo: ")
			
			
			
			
			#ingresar las coordenadas de los disparos
			
			#coordenadas dist1
			
			print("Coordenadas Distancia 1 \n")
			print('---------------------------')
			dist1_x = float(input("Ingrese coordenada x: "))
			dist1_y = float(input(" Ingrese coordenada y: "))
			
			
			
			
			#coordenadas dist2
			
			print("Coordenadas Distancia 2 \n")
			print('---------------------------')
			dist2_x = float(input("Ingrese coordenada x: "))
			dist2_y = float(input("Ingrese coordenada y: "))
			
			# coordenadas dist3
			
			print("Coordenadas Distancia 3 \n")
			print('---------------------------')
			dist3_x = float(input("Ingrese coordenada x: "))
			dist3_y = float(input("Ingrese coordenada y: "))
			
			
			
			
			
			# Se guarda la distancia al origen
			
			# verificar la formula de distancia###########################################################################
			
			participante["Disp1"] = funciones.calculo_disparo(dist1_x, dist1_y )
			participante["Disp2"] = funciones.calculo_disparo(dist2_x, dist2_y)
			participante["Disp3"] = funciones.calculo_disparo(dist3_x, dist3_y)
				
				
			
			participante["MejorDisp"] = funciones.mejor_disparo(participante["Disp1"] ,participante["Disp2"],participante["Disp3"])
			
			
			participante["PromDisp"] = funciones.promedio(participante["Disp1"] ,participante["Disp2"],participante["Disp3"])
			
			
			
			
		except:
			print("Debe ingresar un numero entre 0 y 999 ")
			
			continue
			
		listado.append(participante)
		
		salir = input("Desea salir ? ingrese si o no \n")
		print("")
		
	#Aca muestra el listado
	for elemento in listado:
		print(elemento)
	
	
	return listado
	



def podio(listado):
	intercambios = True
	numPasada = len(listado)-1
	cont = 0
	
	while numPasada > 0 and intercambios:
		intercambios = False
		for k in range(numPasada):
			cont += 1
			if listado[k]["MejorDisp"] < listado[k + 1]["MejorDisp"]:
				intercambios = True
				listado[k], listado[k + 1]= listado[k + 1], listado[k]
		numPasada = numPasada - 1
		
	
	primeros_puestos = listado[0:3]
	
	
	print("Podio: ")
	'''
	f = open ("podio.txt", "w")
	
	for a in primeros_puestos:
		f.write(a)
	f.close()
	'''
	for i in range(len(primeros_puestos)):
		print("Numero: ",listado[i]["numero"],"nombre: ",listado[i]["nombre"],"Mejor Disparo: ", listado[i]["MejorDisp"])
	
	
	# guardarlo en un archivo 
	
	MyFile=open('podio.txt','w')

	MyFile.writelines(primeros_puestos)
	MyFile.close()
	
	return listado
	'''
	Mostrar el podio de los ganadores (los 3 primeros) en función del Mejor Disparo (Nro Participante, Nombre, Apellido y Mejor disparo). 
	Se pide informar por pantalla y en un archivo de texto.
	
	
	Opcional: Mejorar el punto a) asumiendo que se puede dar el caso en que dos participantes tengan el mismo Mejor Disparo,
	ordenar también por mejor promedio.

	'''


	

def ultimo_participante(listado): # el de la peor puntuacion
	# hacer lista con los elementos que necesito ???? #####################################################
	intercambios = True
	numPasada = len(listado)-1
	cont = 0
	
	while numPasada > 0 and intercambios:
		intercambios = False
		for k in range(numPasada):
			cont += 1
			if listado[k]["MejorDisp"] < listado[k + 1]["MejorDisp"]:
				intercambios = True
				listado[k], listado[k + 1]= listado[k + 1], listado[k]
		numPasada = numPasada - 1
	
	#accede al ultimo elemento de listado
	ultimo = listado[-1]
	
	print("ultimo",ultimo)
	# no funciona cuando la lista tiene mas de un elemento
	#print("Ultimo participante.Nombre: " + ultimo["nombre"][0] + " Apellido: " + ultimo["apellido"][0] + "Mejor Disparo" + ultimo[0])
	
	
	'''
	Informar quien fue el último (Nro Participante, Nombre, Apellido y Mejor disparo).
	'''


	
def cantidad_hombres(listado):# si funciona
	#cantidad participantes
	cantidad_participantes = len(listado)
	
	
	
	#cantidad hombres
	cantidad_hombres = 0

	for elemento in listado:
		if elemento["sexo"] == "M" or elemento["sexo"] == "m":
			cantidad_hombres = cantidad_hombres + 1
			
	


	print("Cantidad de participantes: ", cantidad_participantes)
	print("Cantidad de hombres: ", cantidad_hombres)
	
	return cantidad_participantes, cantidad_hombres
	


def edad_mujeres(listado):
	#Informar edad promedio de las mujeres.
	
	listado_mujeres = []
	suma = 0
	
	
	for elemento in listado:
		if elemento["sexo"] == "F" or elemento["sexo"] == "f":
			listado_mujeres.append(elemento["edad"])
			
			
	for elemento in listado_mujeres:
		suma = sum(listado_mujeres)
		
		promedio_mujeres = suma /len(listado_mujeres)
			

	print("Promedio edad mujeres: ", promedio_mujeres)
	
	
def listadoPorEdad(listado): # ordena de mayor a menor!!!!!!!!!!!! pero no de menor a mayor
	#Mostrar el listado de todos los participantes ordenados por edad.
	
	intercambios = True
	numPasada = len(listado)-1
	cont = 0
	
	while numPasada < 0 and intercambios:
		intercambios = False
		for k in range(numPasada):
			cont += 1
			if listado[k]["edad"] < listado[k + 1]["edad"]:
				intercambios = True
				listado[k], listado[k + 1]= listado[k + 1], listado[k]
		numPasada = numPasada - 1
		
	print("Listado por Edad: ")
	for i in range(len(listado)):
		
		print("Numero: ",listado[i]["numero"],"nombre: ",listado[i]["nombre"],"Edad: ", listado[i]["edad"])
	
	return listado
		
	



def promedio_general(listado):# si funciona
	
	#promedio de todos los disparos
	# hago lista de los disp1, disp2, disp3
	lista =[]
	
	suma_total = 0
	
	for elemento in listado:
		lista.append(elemento["Disp1"])
		lista.append(elemento["Disp2"])
		lista.append(elemento["Disp3"])
		
		suma_total = sum(lista)
		promedio_disparos = suma_total /len(lista)
	
	#Mostrar los participantes cuyo promedio de disparo sea mayor al promedio general. + de 1 !!!!!!!!!!!!!!!!!!!!!!
	
	for elemento in listado:
		if elemento["PromDisp"] > promedio_disparos:
			print("El promedio del participante {0} es mayor  al promedio general".format(elemento["nombre"]))
		
		

	print("promedio general de disparos ", promedio_disparos)
	
	
	
	
	
	

resultado = carga_datos()
print("")
podio = podio(resultado)
print("")
#participantes = cantidad_hombres(resultado)
print("")
#ultimo = ultimo_participante(resultado)
print("")
#edad_mujeres = edad_mujeres(resultado)
print("")
#suma_disp1 = promedio_general(resultado)
print("")
#orden = listadoPorEdad(resultado)