from config import *


class Recompensa:
    def __init__(self):
        self.puntuacio = 0
        self.retorn_des = 0

    def sumar_recompensa(self, reward):
        self.puntuacio += reward

    def mostrar_puntuacio(self):
        return self.puntuacio, self.retorn_des

    def retorn_descomptat(self, reward, iteraccio):
        self.retorn_des += reward * (gamma**iteraccio)
        # print('calculant',self.retorn_des, '+', reward,'*', gamma,'**', iteraccio)


import numpy as np


def state_Value_calc(reward, Policy_prob, state_value):
    new_state_value = reward + gamma * np.dot(Policy_prob, state_value)
    return new_state_value


# def Matrix_Policy_prob():
#     for i in range(tamany_graella[0] * tamany_graella[1]):
#         Personatge.estat_actual = Estat.graella[i][j]
#         policy = Personatge.estat_actual.propietats["policy"]
#         policies_probabilitats = Personatge.llegir_policy(policy)
#         probabilitats = list(policies_probabilitats.values())

#         Policy_prob_matrix[i][j] = policies_probabilitats[i][j]
