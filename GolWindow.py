import sys
from PyQt5.QtWidgets import QMainWindow
from golView import Ui_MainWindow
from Model import Model
from GolTimer import GolTimer

class GolWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # la view è generata attraverso QtDesigner
        self.ui.setupUi(self)

        self.model = Model()  # inizializza model e timer 
        self.timer = GolTimer()

        self.ui.Board.set_board(self.model, self.timer)  # setta model e timer per la board

        self.timer.timeout.connect(self.model.update)      # connette timeout del timer al modello 
        self.ui.PlayButton.clicked.connect(self.press_play)  # connette buttons e slider ai rispettivi slot
        self.ui.StopButton.clicked.connect(self.press_stop)
        self.ui.ClearButton.clicked.connect(self.press_clear)
        self.ui.horizontalSlider.valueChanged.connect(self.changeFrameRate)
        self.timer.timeout.connect(self.ui.Board.updateView)  # connette timeout all'update della view 

    def press_play(self):  # fa partire il loop quando il bottone play viene clickato
        self.timer.play()

    def press_stop(self):  # mette in pausa il loop quando il bottone stop viene clickato
        self.timer.stopping()

    def press_clear(self):  # svuota la board quando il bottone clear viene clickato
        self.model.clear()
        self.ui.Board.updateView()  
        self.timer.running = False  # ferma il gioco per poter editare la board

    def changeFrameRate(self):  # cambia il frameRate quando è cambiato il valore dello slider
        self.timer.timerValue = 120 - self.ui.horizontalSlider.value()




