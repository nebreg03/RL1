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
for fila in range(tamany_graella[0]):
     for columna in range(tamany_graella[1]):
         execucio += 1
         subprocess.run(
             ["python", "run.py", f"{fila},{columna}"], capture_output=True, text=True
        )
#for fila in range(tamany_graella[0]):
#    execucio += 1
#    subprocess.run(["python", "run.py", f"{fila},{1}"], capture_output=True, text=True)

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

for idx, resultat in enumerate(resultats, start=1):
    print(f"Execució {idx} a {resultat['Inici']}: Return: {resultat['Puntuacio final']}, Discounted Return: {resultat['Discounted error']}")
# print(resultats)
max_execucio_info = None
# Obtenir l'element amb el Discounted error més gran
max_execucio_info = max(resultats, key=lambda x: x['Discounted error'])
# Imprimir les dades de l'element
print(f"La millor casella de sortida és: {max_execucio_info['Inici']}")


print("Anem a passar-nos el joc!\n\n")
# Obtenir les coordenades de l'execució amb el Discounted error més gran
coor = max_execucio_info['Inici'][1:-1].split(',')
fila = coor[0].strip()
columna = coor[1].strip()

# Executar run.py amb les coordenades corresponents i guardar l'output
result = subprocess.run(
    ["python", "run.py", f"{fila},{columna}"],
    capture_output=True,
    text=True
)

# Imprimir l'output
print(result.stdout)
