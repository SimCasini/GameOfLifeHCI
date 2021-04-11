import sys
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QImage, qRgb
from Model import Model

class GolBoard(QLabel):
    def __init__(self, QWidget):
        super().__init__()
        self.w = 0  # larghezza griglia
        self.he = 0 # altezza griglia

    def set_board(self, model, timer):
        self.model = model
        self.timer = timer
        self.updateView() # imposta il primo frame all'avvio

    def mousePressEvent(self, event): # override dello slot per mouse press event
        if self.timer.running == False and event.buttons() == QtCore.Qt.LeftButton: # se il gioco è in pausa e uso il tasto sinistro per attivare celle
            i = event.pos().y() 
            j = event.pos().x() 
            if i > 0 and j > 0 and i < self.pixmap().height() and j < self.pixmap().width(): # verifica se il mouse è dentro la pixmap
                i = int(i * self.he / self.pixmap().height())  # converte le coordinate in quelle della griglia 
                j = int(j * self.w / self.pixmap().width())
                self.model.activate_pixel(i, j)  # attivo la cella corrispondente
                self.updateView()

        if self.timer.running == False and event.buttons() == QtCore.Qt.RightButton: # se il gioco è in pausa e uso il tasto destro per disattivare celle
            i = event.pos().y() 
            j = event.pos().x()
            if i > 0 and j > 0 and i < self.pixmap().height() and j < self.pixmap().width():
                i = int(i * self.he / self.pixmap().height())
                j = int(j * self.w / self.pixmap().width())
                self.model.deactivate_pixel(i, j)  # disattiva la cella corrispondente
                self.updateView()

    def mouseMoveEvent(self, event): # override dello slot per mouse move event per quando si muove il mouse tenendo premuto
        if self.timer.running == False and event.buttons() == QtCore.Qt.LeftButton: # se il gioco è in pausa e uso il tasto sinistro per attivare celle
            i = event.pos().y() 
            j = event.pos().x() 
            if i > 0 and j > 0 and i < self.pixmap().height() and j < self.pixmap().width():
                i = int(i * self.he / self.pixmap().height())
                j = int(j * self.w / self.pixmap().width())
                self.model.activate_pixel(i, j)
                self.updateView()

        if self.timer.running == False and event.buttons() == QtCore.Qt.RightButton : # se il gioco è in pausa e uso il tasto destro per disattivare celle
            i = event.pos().y() 
            j = event.pos().x() 
            if i > 0 and j > 0 and i < self.pixmap().height() and j < self.pixmap().width():
                i = int(i * self.he / self.pixmap().height())
                j = int(j * self.w / self.pixmap().width())
                self.model.deactivate_pixel(i, j)
                self.updateView()

    def updateView(self): # converte la griglia (cioè un array) in una QPixmap che viene mostrata nella QLabel
        grid = self.model.get_grid()
        self.he = grid.shape[0]
        self.w = grid.shape[1]
        qImage = self.toQImage(grid) # prima converte la griglia in una QImage
        qPix = QPixmap.fromImage(qImage) # dalla QImage ottiene la QPixmap
        self.setPixmap(qPix.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.FastTransformation)) # setta la pixmap

    def toQImage(self, im):  # im è l'array da convertire in una QImage bianca e nera
        gray_color_table = [qRgb(i, i, i) for i in range(256)]

        if im is None:
            return QImage()
        else:
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
            qim.setColorTable(gray_color_table)
            return qim


    

