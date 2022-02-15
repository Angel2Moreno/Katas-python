
#1
asteroide = 49
if asteroide > 25:
    print('Se acerca a velocidades peligrosas!')
else:
    print('Sin peligro')
    
#2
asteroide = 19
if asteroide > 20:
    print('Hay una luz  en el cielo!')
elif asteroide == 20:
    print('Hay una luz mágica en el cielo!')
else:
    print('¡Nada que ver aquí!')
    
#3
velocidad_asteroide = 25
tamano_asteroide = 40
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')