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

    def accio_reward(self):
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
            nova_fila, nova_columna = self.estat_actual.fila, self.estat_actual.columna
            print("He sumat", reward_fora, "a la recompensa")
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

    def llegir_policy(self, policy):
        policies_probabilitats = next(
            (
                p[1]
                for p in policy
                if p[0] == (self.estat_actual.fila, self.estat_actual.columna)
            ),
            None,
        )
        return policies_probabilitats

    def obtenir_nova_posicio(self, policy):
        nova_fila, nova_columna = self.estat_actual.fila, self.estat_actual.columna

        # Obté les polítiques i les probabilitats de la cèl·lula actual
        policies_probabilitats = self.llegir_policy(policy)

        print(policies_probabilitats)
        print("Estava a", self.estat_actual.fila, self.estat_actual.columna)

        probabilitats = list(policies_probabilitats.values())
        moviment = random.choices(list(policies_probabilitats.keys()), probabilitats)[0]
        print("He triat ", moviment)
        # Mou el personatge segons la nova política
        nova_fila, nova_columna = self.moure(moviment, nova_fila, nova_columna)
        return nova_fila, nova_columna

    def moure(self, moviment, nova_fila, nova_columna):
        if moviment == "U":
            nova_fila -= 1
        elif moviment == "D":
            nova_fila += 1
        elif moviment == "R":
            nova_columna += 1
        elif moviment == "L":
            nova_columna -= 1
        elif moviment == "S":
            pass
        if self.esta_fora_del_limit(nova_fila, nova_columna):
            print("No em puc moure, hi ha una barrera")
        else:
            print("Aniré a", nova_fila, nova_columna)
        return nova_fila, nova_columna

    def ha_arribat_a_la_final(self):
        return (
            self.estat_actual.fila == tamany_graella[0] - 1
            and self.estat_actual.columna == tamany_graella[1] - 1
        )

    def esta_fora_del_limit(self, nova_fila, nova_columna):
        return (
            nova_fila < 0
            or nova_fila >= tamany_graella[0]
            or nova_columna < 0
            or nova_columna >= tamany_graella[1]
        )

    # function that determines which moviment must be done to go to the next state
    def trobar_moviment(estat1, estat2):
        if estat1 == estat2:
            return "S"
        dif_fila = estat2[0] - estat1[0]
        dif_col = estat2[1] - estat1[1]
        if abs(dif_fila) + abs(dif_col) > 1:
            return "0"
        if dif_fila == -1:
            return "U"
        if dif_fila == 1:
            return "D"
        if dif_col == -1:
            return "L"
        if dif_col == 1:
            return "R"


# estat_Test = (0, 0)
# estat_Test2 = (0, 1)
# moviment = Personatge.trobar_moviment(estat_Test, estat_Test2)
# policy = Personatge.llegir_policy(moviment)
