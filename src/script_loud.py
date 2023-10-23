import subprocess
from config import *

resultats = []
execucio = 0
max_discounted_error = -float("inf")  # Inicialitza amb el valor mínim possible
max_execucio_info = None
prev_max_execucio_info = None  # Initialize previous value to None


# delete values from resultats.txt
with open("resultats.txt", "w") as file:
    file.write("")

# Recorre totes les cel·les possibles
print("Entrenant")
# for fila in range(tamany_graella[0]):
#     for columna in range(tamany_graella[1]):
#         execucio += 1
#         subprocess.run(
#             ["python", "run.py", f"{fila},{columna}"], capture_output=True, text=True
#         )
for fila in range(tamany_graella[0]):
    execucio += 1
    subprocess.run(["python", "run.py", f"{fila},{1}"], capture_output=True, text=True)

    # Afegit: Llegeix el fitxer de resultats
with open("resultats.txt", "r") as file:
    entry = {}
    for line in file:
        key, value = line.strip().split(": ")
        # Si és el principi d'una nova entrada
        if key == "Inici":
            if entry:
                resultats.append(entry)
            entry = {"Inici": value}
        else:
            entry[key] = float(value)

# Afegir l'última entrada
if entry:
    resultats.append(entry)

# print value of "Discounted Return" for Discounted error = 0.0
# discounted_return_0 = [
#     value for key, value in resultats if key == "Discounted Return" and value == "0.0"
# ][0]
# print(f"Discounted Return per a Discounted error = 0.0: {discounted_return_0}")

# print(resultats)
max_discounted_error = -float("inf")  # Inicialitza amb el valor mínim possible
max_execucio_info = None

# Recorre les dades de resultats
for key, value in resultats:
    print(f"{key}: {value}")
    if key == "Discounted error" and float(value) > max_discounted_error:
        max_discounted_error = float(value)
        max_execucio_info = resultats

# Imprimeix l'execució amb el valor de discounted error més gran
if max_execucio_info is not None:
    print(f"Execució amb el valor de discounted error més gran:")
    for key, value in max_execucio_info:
        print(f"{key}: {value}")
else:
    print("No s'ha trobat cap execució amb Discounted error.")
