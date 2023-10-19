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
        self.retorn_des += reward*(gamma**iteraccio)
        # print('calculant',self.retorn_des, '+', reward,'*', gamma,'**', iteraccio)
        
    
