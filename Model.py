import numpy as np
from scipy import signal

ALIVE = 255   # valore della cella viva

class Model:
    def __init__(self, x=100, y=150):
        self.x = x
        self.y = y
        self._grid = np.zeros((self.x,self.y), dtype=np.uint8)

        # configurazione glider gun
        glider_gun = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]) * ALIVE

        self._grid[1:10, 1:37] = glider_gun  # setta come prima configurazione della griglia quella con un glider gun in alto a sinistra

        self.kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])  # kernel usato per la convoluzione
        self.clear_state = np.zeros((self.x,self.y), dtype=np.uint8)  # stato ottenuto premenendo clear è la griglia vuota
        #self.clear_state = np.copy(self._grid)

    def update(self):  # calcola lo stato successivo della griglia attraverso la convoluzione col kernel e applicando le regole di Conway
        conv = np.asmatrix(signal.convolve2d(self._grid, self.kernel, 'same')) # matrice ottenuta con la convoluzione col kernel
        self._grid[conv <= ALIVE] = 0  # se ha zero o un solo vicino la cella muore
        self._grid[conv >= 4 * ALIVE] = 0  # se ha 4 o piu vicini la cella muore
        self._grid[conv == 3 * ALIVE] = ALIVE  # se ha 3 vicini la cella diventa viva 

    def get_grid(self): # restituisce la griglia
        return self._grid

    def clear(self): # restituisce lo stato clear cioè la griglia vuota 
        self._grid = np.copy(self.clear_state)

    def deactivate_pixel(self, i, j): # pone a zero il pixel di coordinate i,j
        self._grid[i, j] = 0


    def activate_pixel(self, i, j): # rende vivo il pixel di coordinate i,j
        self._grid[i, j] = ALIVE 
