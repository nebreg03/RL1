#Aquest scrip mostra els resultats mentre s'entrena

import subprocess
from config import *
from run import *
from tqdm import tqdm

resultats = []

# Recorre totes les cel·les possibles
print("Entrenant")
for fila in tqdm(range(tamany_graella[0])):
    for columna in range(tamany_graella[1]):
        result = subprocess.run(['python', 'run.py', f'{fila},{columna}'], capture_output=True, text=True)
        output = result.stdout.strip().split('\n')
        puntuacio_final = round(float(output[-2].split(': ')[1]), 3)
        discounted_return = round(float(output[-1].split(': ')[1]), 3)
        resultats.append((puntuacio_final, discounted_return))

# Imprimeix tots els resultats
for idx, resultat in enumerate(resultats, start=1):
    print(f'Execució {idx} a ({fila},{columna}): Return: {resultat[0]}, Discounted Return: {resultat[1]}')
