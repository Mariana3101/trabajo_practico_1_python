import math

#funcion Calculo_disparo
#recibe las coordenadas 
#retorna la distancia al centro


def calculo_disparo(x,y ):
	
	distancia = math.sqrt((x**2 + y**2)**2)
	return distancia





#funcion Calculo_Mejor_Disparo
# recibe las 3 distancias 
#retorna la mejor 

def mejor_disparo(dist1, dist2, dist3):
	if dist1 > dist2 and dist1 > dist3:
		mejor_distancia = dist1
	elif dist2 > dist1 and dist2 >dist3:
		mejor_distancia = dist2
	else:
		mejor_distancia = dist3
		
	
	return mejor_distancia
	
	
	
	
	
	
# Funcion Promedio_Disparo
#recibe las 3 distancias
# retorna el promedio 





def promedio(dist1, dist2, dist3):

	promedio = (dist1  + dist2 + dist3) /3
	
	return promedio 
	
	
	
	











