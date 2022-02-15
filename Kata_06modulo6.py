#1
planetas = ['mercurio','venus','tierra','marte','jupiter','saturno','urano','neptuno']
print(planetas, 'que hay')
planetas.append('pluton')
print(planetas[8], 'planeta que se agrego al arreglo \n')
print(planetas)

#2


planets = ['mercurio','tierra','martes','jupiter','saturno','neptuno']
planetaAgrega = input('Dame un planeta ')
planets.append(planetaAgrega)
planetaBusqueda = planets.index(planetaAgrega)

print('planetas cercas al sol '+ planetaAgrega)
print(planets[0:planetaBusqueda])

print('planetas lejos del sol '+ planetaAgrega)
print(planets[planetaBusqueda+1:])