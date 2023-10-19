import sys
import random
from estat import *
from personatge import *
from recompensa import *
from config import llegir_policies


print("Inici de càrrega")
print("Llegint policies...")
policies = llegir_policies()
print("Creant graella...")
graella = crear_graella(policies)

print("Determinant inici")
if len(sys.argv) > 1:
    # Llegeix les coordenades d'inici com una cadena de text
    inici_str = sys.argv[1]

    # Converteix la cadena de text a una tupla de coordenades
    inici = tuple(map(int, inici_str.split(',')))
else:
    inici = (1, 0)

estat_inicial = graella[inici[0]][inici[1]]

print("Afegint físiques...")
afegir_fisiques(graella, inici)
print("Actualitzant recompenses...\n")
actualitzar_rewards(graella, inici)
# print("Mostrant graella...")
print("Començant a:", inici)
mostrar_graella(graella)

print("Iniciant recompensa")
recompensa = Recompensa()
print("Iniciant personatge\n")
personatge = Personatge(graella, estat_inicial, recompensa)

try:
    while True:
        print("Vaig a moure'm!")
        nova_fila, nova_columna=personatge.moure()
        print("Pasa feta!\n")
        
        if personatge.ha_arribat_a_la_final():
            break

        if personatge.esta_fora_del_limit(nova_fila, nova_columna):
            break

except MarejatError as e:
    print(e)

puntuacio_final, discounted_error = recompensa.mostrar_puntuacio()

print(f'Puntuació final: {puntuacio_final}')
print(f'Discounted retunr: {discounted_error}')
