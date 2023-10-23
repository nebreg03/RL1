import subprocess
from config import *

resultats = []
execucio = 0
max_discounted_error = -float("inf")  # Inicialitza amb el valor mínim possible
max_execucio_info = None


# delete values from resultats.txt
with open("resultats.txt", "w") as file:
    file.write("")

# Recorre totes les cel·les possibles
print("Entrenant")
for fila in range(tamany_graella[0]):
    for columna in range(tamany_graella[1]):
        execucio += 1
        subprocess.run(
            ["python", "run.py", f"{fila},{columna}"], capture_output=True, text=True
        )

        # Afegit: Llegeix el fitxer de resultats
with open("resultats.txt", "r") as file:
    for line in file:
        key, value = line.strip().split(": ")
        resultats.append((key, value))

        # print(
        #     f"Execució {execucio} a ({fila},{columna}): Return: {puntuacio_final}, Discounted Return: {discounted_return}"
        # )
for key, value in resultats:
    if key == "Discounted error" and float(value) > max_discounted_error:
        max_discounted_error = float(value)
        max_execucio_info = resultats[-1]  # Guarda tota la info de l'execució
        print(
            "Nova execució amb el valor de discounted error més gran:",
            max_execucio_info,
        )

for key, value in resultats:
    print(f"{key}: {value}")

print
