import random
from config import *



class Estat:
    def __init__(self, fila, columna, policies):
        self.fila = fila
        self.columna = columna
        self.propietats = {
            "policy": policies,
            "reward": 0,
            "fisica": "    -    "
        }
    
    def afegir_propietat(self, clau, valor):
        self.propietats[clau] = valor
        

    def mostrar_propietats(self):
        return self.propietats
def crear_graella(policies):
    graella = [[Estat(i, j, policies) for j in range(tamany_graella[1])] for i in range(tamany_graella[0])]
    return graella


def afegir_fisiques(graella,inici):
    estat_inici = inici
    estat_final = graella[tamany_graella[0]-1][tamany_graella[1]-1]

    # prohibit_count = 0
    # while prohibit_count < max_prohibits:
    #     estat = graella[random.randint(0, tamany_graella[0]-1)][random.randint(0, tamany_graella[1]-1)]
    #     if estat.propietats["fisica"] == "    -    " and estat != estat_inici and estat != estat_final:
    #         estat.afegir_propietat("fisica", " prohibit")
    #         prohibit_count += 1 
    fila, columna = casella_prohibit
    estat = graella[fila][columna]
    if estat.propietats["fisica"] == "    -    " and estat != estat_inici and estat != estat_final:
            estat.afegir_propietat("fisica", " prohibit")

def actualitzar_rewards(graella,inici):
    for fila in graella:
        for estat in fila:
            # if (estat.fila, estat.columna) == inici:
            #     estat.propietats["fisica"] = "  inici  "
            #     estat.propietats["reward"] = reward_inici
            if (estat.fila, estat.columna) == (tamany_graella[0]-1, tamany_graella[1]-1):
                estat.propietats["fisica"] = "  final  "
                estat.propietats["reward"] = reward_final
            elif estat.propietats["fisica"] == " prohibit":
                estat.propietats["reward"] = reward_prohibit
            elif estat.propietats["fisica"] == "    -    ":
                estat.propietats["reward"] = reward_blank



def mostrar_graella(graella):
    for fila in graella:
        for estat in fila:
            # print(f"| ({estat.propietats['policy']}, {estat.propietats['reward']}, {estat.propietats['fisica']})", end=" ")
            print(f"| ({estat.propietats['reward']}, {estat.propietats['fisica']})", end=" ")

        print("|")
    print("\n")


