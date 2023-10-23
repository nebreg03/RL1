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
    for line in file:
        key, value = line.strip().split(": ")
        resultats.append((key, value))

        # print(
        #     f"Execució {execucio} a ({fila},{columna}): Return: {puntuacio_final}, Discounted Return: {discounted_return}"
        # )

for key, value in resultats:
    print(f"{key}: {value}")

# get a list of all "Discounted Return" values
discounted_error_list = [
    float(value) for key, value in resultats if key == "Discounted error"
]
# print the maximum value and also "Inici" value of the maximum value
max_discounted_error = max(discounted_error_list)
max_execucio_info = [
    key for key, value in resultats if value == str(max_discounted_error)
][0]
print(f"Maximum discounted error: {max_discounted_error}")
print(f"Execucio amb el valor màxim: {max_execucio_info}")

# print value of "Discounted Return" for Discounted error = 0.0
# discounted_return_0 = [
#     value for key, value in resultats if key == "Discounted Return" and value == "0.0"
# ][0]
# print(f"Discounted Return per a Discounted error = 0.0: {discounted_return_0}")

print(resultats)
