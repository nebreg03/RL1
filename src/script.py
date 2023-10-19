import subprocess
from config import *
from run import *


# Defineix una llista per emmagatzemar els resultats
resultats = []

# Itera a través de totes les cel·les de la graella com a inici
import subprocess

# Defineix una llista per emmagatzemar els resultats
resultats = []

# Recorre totes les cel·les possibles
for fila in range(tamany_graella[0]):
    for columna in range(tamany_graella[1]):
        # Executa run.py amb les coordenades de inici
        result = subprocess.run(['python', 'run.py', f'{fila},{columna}'], capture_output=True, text=True)
        print(f"Execució amb inici a la cel·la ({fila}, {columna})")
        output = result.stdout.strip().split('\n')
        puntuacio_final = round(float(output[-2].split(': ')[1]), 3)
        discounted_return = round(float(output[-1].split(': ')[1]), 3)
        resultats.append((puntuacio_final, discounted_return))

# Imprimeix tots els resultats
for idx, resultat in enumerate(resultats, start=1):
    print(f'Execució {idx}: Return: {resultat[0]}, Discounted Return: {resultat[1]}')
