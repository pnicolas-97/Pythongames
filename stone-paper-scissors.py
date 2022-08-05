import random

options = ('piedra','papel','tijera')
machine = random.choice(options)
print('*' * 31)
print('Eliga... Piedra, Papel o tijera')
print('*' * 31)
print()
player = input('Ingresar opcion: ').lower()


while player not in options:
    print()
    print('Error... cargue una OPCION VALIDA')
    print('PIEDRA','PAPEL','TIJERA')
    player = input('Ingresar opcion: ').lower()

if machine == player:
    print('Empate')
elif ((machine == 'piedra' and player == 'tijera')
    or (machine == 'tijera' and player == 'papel')
    or (machine == 'papel' and player == 'piedra')):
    print('Machine wins')

else:
    print('Player Wins')
print('La maquina eligio: ',machine)
print('Usted eligo: ',player)
