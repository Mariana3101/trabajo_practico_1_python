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
			
			# Excepcion para que no permita ingresar participantes mayor a 999
			if participante["numero"] > 999:
				raise Exception("Debe ingresar un numero entre 0 y 999 ")
			
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
			print('---------------------------')
			print("Coordenadas Distancia 2 \n")
			print('---------------------------')
			dist2_x = float(input("Ingrese coordenada x: "))
			dist2_y = float(input("Ingrese coordenada y: "))
			
			# coordenadas dist3
			print('---------------------------')
			print("Coordenadas Distancia 3 \n")
			print('---------------------------')
			dist3_x = float(input("Ingrese coordenada x: "))
			dist3_y = float(input("Ingrese coordenada y: "))
			
			
			
			
			
			# Se guarda la distancia al origen
			

			
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
		
	
	
	return listado
	


#F
'''
Mostrar el podio de los ganadores (los 3 primeros) en función del Mejor Disparo (Nro Participante, Nombre, Apellido y Mejor disparo).
Se pide informar por pantalla y en un archivo de texto.
'''

def podio(listado):
	# Ordenamiento por MejorDisp
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
		
	
	primeros_puestos = (listado[0:3])
	
	print("Los tres primeros puestos son \n")
	
	#Imprime los tres primeros puestos
	for i in range(len(primeros_puestos)):
		print("Numero: ",listado[i]["numero"],"nombre: ",listado[i]["nombre"],"Mejor Disparo: ", listado[i]["MejorDisp"])
		
	return listado

#F	
# se guardan los tres primeros elementos
def guardar_podio(listado):

	
	primeros_puestos = []
	
	primeros_puestos.append(listado[0:3])
	
	
	MyFile=open('output.txt','w')
	
	MyFile.write(str(listado))
	
	MyFile.close()
	
	
	
#G
'''
Informar quien fue el último (Nro Participante, Nombre, Apellido y Mejor disparo).
'''
def ultimo_participante(listado): # el de la peor puntuacion
	#ordenamiento para tener el  participante con peor puntuacion
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

	
	ultimo_participante= "Numero {}, Nombre {}, Mejor Disparo {}".format(listado[-1]["numero"],listado[-1]["nombre"],listado[-1]["MejorDisp"])
	return ultimo_participante
	


#H - I
'''
Informar cuantos participantes formaron parte del concurso.
Informar cuantos hombres formaron parte del concurso.

'''
def cantidad_participantes(listado):
	#cantidad participantes
	cantidad_participantes = len(listado)
	
	return cantidad_participantes
	
def cantidad_hombres(listado):
	
	cantidad_hombres = 0

	for elemento in listado:
		if elemento["sexo"] == "M" or elemento["sexo"] == "m":
			cantidad_hombres = cantidad_hombres + 1
			
	
	return cantidad_hombres

#J
'''
Informar edad promedio de las mujeres.
'''
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
			

	return promedio_mujeres
	
#K
'''
Mostrar el listado de todos los participantes ordenados por edad.
'''

def listadoPorEdad(listado): # ordena de menor a mayor
	
	intercambios = True
	numPasada = len(listado)-1
	cont = 0
	
	while numPasada > 0 and intercambios:
		intercambios = False
		for k in range(numPasada):
			cont += 1
			if listado[k]['edad'] > listado[k + 1]['edad']:
				intercambios = True
				listado[k], listado[k + 1]= listado[k + 1], listado[k]
		numPasada = numPasada - 1
		
	
	return listado
		
	


#L 
'''
Informar el promedio de todos los disparos.

'''
def promedio_disparos(listado):# si funciona
	
	#promedio de todos los disparos
	# hago lista de los disp1, disp2, disp3
	lista =[]
	
	suma_total = 0
	
	for elemento in listado:
		lista.append(elemento["Disp1"])
		lista.append(elemento["Disp2"])
		lista.append(elemento["Disp3"])
		
		suma_total = sum(lista)
		promedio_disparos = round((suma_total /len(lista)),2)
	
	return promedio_disparos
	
	
#M	
#Mostrar los participantes cuyo promedio de disparo sea mayor al promedio general.
def mayor_promedio(listado, promedio_disparos):


	lista_promedios = []
	
	for elemento in listado:
		if elemento["PromDisp"] > promedio_disparos:
			lista_promedios.append(elemento["nombre"])
			lista_promedios.append(elemento["apellido"])
		    
	return lista_promedios

		
		
		
		
resultado = carga_datos()
print("")
podio = podio(resultado)
print("")
guardar_datos_podio = guardar_podio(resultado)
print("")
ultimo_participante = print("El participante con peor disparo es: ",ultimo_participante(resultado),"\n")

cantidad_participantes = print("Cantidad de participantes: ",cantidad_participantes(resultado),"\n")

cantidad_hombres = print("Cantidad de hombres que participaron: ", cantidad_hombres(resultado),"\n")

promedio_edad_mujeres = print("Promedio edad Mujeres: ",edad_mujeres(resultado),"\n")

listado_Por_Edad = print("Listado ordenado por edad(de menor a mayor ): \n",listadoPorEdad(resultado))

el_promedio_disparos = print("El promedio general de disparos es ",promedio_disparos(resultado),"\n")

mayor_promedio = print("Lista de participantes con promedio de disparos mayor al promedio general \n", mayor_promedio(resultado,(promedio_disparos(resultado))))