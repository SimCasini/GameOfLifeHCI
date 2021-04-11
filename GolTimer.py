import sys
from PyQt5.QtCore import QTimer


class GolTimer(QTimer):
    def __init__(self):
        super().__init__()
        self.running = False  # variabile usata per sapere lo stato del gioco, se è in pausa o meno
        self.timerValue = 100  # intervallo di timeout in ms del timer
        self.timeout.connect(self.loop)  # timeout signal connesso a loop
        self.setSingleShot(True)  # il timer viene attivato solo una volta

    def loop(self): # chiamato ad ogni timeout e se il gioco è running fa il restart del timer
        if self.running:
            self.start(self.timerValue)

    def play(self):
        if self.running == False:  # se è premuto quando il gioco è fermo allora fa partire il timer
            self.start(self.timerValue)
            self.running = True

    def stopping(self):
        if self.running == True:   # se è premuto quando è running allora stoppa il timer
            self.stop()
            self.running = False

    



