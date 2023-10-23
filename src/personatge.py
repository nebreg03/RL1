from recompensa import Recompensa
from config import *
from estat import *
import random
class MarejatError(Exception):
    pass

random.seed(42)


class Personatge:
    def __init__(self, graella, estat_inicial, recompensa):
        self.graella = graella
        self.estat_actual = estat_inicial
        self.caselles_visitades = {}
        self.recompensa = recompensa
        self.iteraccio = 0
    
    def moure(self):
        self.iteraccio += 1
        reward = self.estat_actual.propietats["reward"]
        self.recompensa.sumar_recompensa(reward)
        self.recompensa.retorn_descomptat(reward, self.iteraccio)
        print("He sumat", reward, "a la recompensa")
        print("Llegint policy...")
        policy = self.estat_actual.propietats["policy"]
        nova_fila, nova_columna = self.obtenir_nova_posicio(policy)

        if (nova_fila, nova_columna) in self.caselles_visitades:
            self.caselles_visitades[(nova_fila, nova_columna)] += 1
        else:
            self.caselles_visitades[(nova_fila, nova_columna)] = 1

        if self.caselles_visitades[(nova_fila, nova_columna)] > mareig:
            raise MarejatError("M'he marejat!")

        


        if self.esta_fora_del_limit(nova_fila, nova_columna):
            self.recompensa.sumar_recompensa(reward_fora)
            self.recompensa.retorn_descomptat(reward_fora, self.iteraccio)
            print("He sumat", reward_fora, "a la recompensa")
            print("El personatge s'ha trobat amb una barrera")
        else:
            self.estat_actual = self.graella[nova_fila][nova_columna]
            if self.ha_arribat_a_la_final():
                self.recompensa.sumar_recompensa(reward_final)
                self.recompensa.retorn_descomptat(reward_final, self.iteraccio)
                print("He sumat", reward_final, "a la recompensa")
                print("Personatge ha arribat a la casella final")
        return nova_fila, nova_columna




    def mostrar_posicio(self):
        return f"Personatge a l'estat ({self.estat_actual.fila}, {self.estat_actual.columna})"
    
    def obtenir_nova_posicio(self, policy):
        nova_fila, nova_columna = self.estat_actual.fila, self.estat_actual.columna

        # Obté les polítiques i les probabilitats de la cèl·lula actual
        policies_probabilitats = next((p[1] for p in policy if p[0] == (self.estat_actual.fila, self.estat_actual.columna)), None)

        print(policies_probabilitats)
        print("Estava a", self.estat_actual.fila,self.estat_actual.columna)

        # Crea una llista amb les probabilitats
        probabilitats = list(policies_probabilitats.values())
        # Selecciona una nova política en funció de les probabilitats
        nova_policy = random.choices(list(policies_probabilitats.keys()), probabilitats)[0]
        print("He triat ", nova_policy)
        # Mou el personatge segons la nova política
        if nova_policy == "U":
            nova_fila -= 1
        elif nova_policy == "D":
            nova_fila += 1
        elif nova_policy == "R":
            nova_columna += 1
        elif nova_policy == "L":
            nova_columna -= 1
        print("Aniré a", nova_fila, nova_columna)
        return nova_fila, nova_columna


    def ha_arribat_a_la_final(self):
        return self.estat_actual.fila == tamany_graella[0] - 1 and self.estat_actual.columna == tamany_graella[1] - 1
    def esta_fora_del_limit(self, nova_fila, nova_columna):
        return nova_fila < 0 or nova_fila >= tamany_graella[0] or nova_columna < 0 or nova_columna >= tamany_graella[1]
