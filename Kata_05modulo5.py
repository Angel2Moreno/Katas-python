from tkinter import Variable


tierra = 149597870
jupiter = 778547200 

distancia = jupiter - tierra
print (distancia) 

print (distancia * 0.621 ,'km') 

# 2
planeta1 = input('introduzca la distancia del sol para el planeta1 en Km ')
planeta2 = input('introduzca la distancia del sol para el planeta2 en Km ')

planeta1 = int(planeta1)
planeta2 = int(planeta2)

distancia2 = planeta2 - planeta1
print(distancia2,'en Km')

distanciaMillas = distancia2 * 0.621 
print(abs(distanciaMillas),'en millas')

